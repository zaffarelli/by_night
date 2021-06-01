let line_jump_code = 'N*L';

/* Callback functions */
function toggleAll(d) {
    if (d.children) {
        d.children.forEach(toggleAll);
        toggle(d);
    }
}

function toggle(d) {
    if (d.children) {
        d._children = d.children;
        d.children = null;
    } else {
        closeSiblings(d);
        d.children = d._children;
        d._children = null;
    }
}

function toggleSimple(d) {
    if (d.children) {
        d._children = d.children;
        d.children = null;
    } else {
        d.children = d._children;
        d._children = null;
        d.children.forEach(toggleSimple);
    }
}

function closeSiblings(d) {
    if (!d.parent)
        return;
    d.parent.children.forEach(function(d1) {
        if (d1 === d || !d1.children)
            return;
        d1._children = d1.children;
        d1.children = null;
    });
}



function wrap(text, width) {
    text.each(function() {
        let text = d3.select(this),
            words = text.text().split(/\s+/).reverse(),
            word,
            line = [],
            lineNumber = 0,
            lineHeight = 1.0, // ems
            x = text.attr("x"),
            dx = text.attr("dx"),
            y = text.attr("y"),
            dy = parseFloat(text.attr("dy")),
            tspan = text.text(null).append("tspan").attr("x", x).attr("y", y).attr("dx", dx).attr("dy", dy + "em");
        while (word = words.pop()) {
            if (word == line_jump_code){
                tspan.text(line.join(" "));
                line= [];
                tspan = text.append("tspan")
                    .attr("x", x)
                    .attr("dx", dx)
                    .attr("y", y)
                    .attr("dy", ++lineNumber * lineHeight + dy + "em")
                    .text('');

            }else{
                line.push(word);
                tspan.text(line.join(" "));
                if (tspan.node().getComputedTextLength() > width) {
                    line.pop();
                    tspan.text(line.join(" "));
                    line = [word];
                    tspan = text.append("tspan")
                        .attr("x", x)
                        .attr("dx", dx)
                        .attr("y", y)
                        .attr("dy", ++lineNumber * lineHeight + dy + "em")
                        .text(word);
                }
            }
        }
    });
}


/* The kindred tree display class */
class KindredLineage {
    constructor(data,parent,collector) {
        let me = this;
        me.parent = parent;
        me.co = collector;
        me.data = data;
        me.init();
    }

    init() {
        let me = this;
        me.root = me.data[0];
        me.boxWidth = 160;
        me.boxHeight = 50;
        me.width = parseInt($(me.parent).css("width"),10);
        me.height = me.width*0.58;
        me.w = me.width*1.5;
        me.h = me.height*1.5;
        me.i = 0;
        me.x = d3.scale.linear().domain([0, me.width]).range([0, me.width]);
        me.y = d3.scale.linear().domain([0, me.height]).range([0, me.height]);
        d3.select(me.parent).selectAll("svg").remove();
        me.vis = d3.select(me.parent).append("svg:svg")
            .attr("viewBox", "0 0 " + me.w + " " + me.h)
            .attr("width", me.width)
            .attr("height", me.height)
            .append("svg:g")
            .attr("transform", "translate(0,0)")
            .call(d3.behavior.zoom().x(me.x).y(me.y).scaleExtent([2, 8]).on("zoom", function(e){
                let nodes = me.vis.selectAll("g.node");
                nodes.attr("transform", function(d){
                    return "translate(" + me.x(d.x) + "," + me.y(d.y) + ")"
                });
                let link = me.vis.selectAll("path.link");
                link.attr("d", function(d){
                    let result = '';
                    let sourceX = me.x(d.target.parent.x);
                    let sourceY = me.y(d.target.parent.y);
                    let targetX = me.x(d.target.x);
                    let targetY = me.y(d.target.y);
                    let halfY = sourceY + (targetY - sourceY) / 2
                    result = "M" + sourceX + "," + sourceY + " C" + sourceX + "," + halfY + " " + targetX + "," + halfY + " " + targetX + "," + targetY;
                    return result;
                });
            }))
            ;
        me.vis.append("rect")
            .attr("class", "overlay")
            .attr("width", me.w)
            .attr("height", me.h)
            .attr("x", 0 )
            .attr("y", 0)
            ;

        me.tree = d3.layout.cluster()
            .size([me.width, me.height]);

        me.diagonal = d3.svg.diagonal()
            .projection(function(d) {
                return [d.x, d.y];
            });
        me.root.x0 = 0;
        me.root.y0 = 0;
    }


    update(source) {
        let me = this;
        me.duration = d3.event && d3.event.altKey ? 5000 : 500;
        me.nodes = me.tree.nodes(me.root).reverse();
        let i = 0;
        me.nodes.forEach(function(d) {
            d.y = d.depth * me.boxHeight * 1;
        });


        me.node = me.vis.selectAll("g.node")
            .data(me.nodes, function(d) {
                return d.id || (d.id = ++i);
            });

        me.nodeEnter = me.node.enter().append("svg:g")
            .attr("class", "node")
            .attr("transform", function(d) {
                return "translate(" + source.x0 + "," + source.y0 + ")";
            });

        me.nodeEnter.append("rect")
            .attr('class', 'band')
            .attr({
                x: -me.boxWidth * 0.5,
                y: -me.boxHeight * 1,
                width: me.boxWidth * 1,
                height: me.boxHeight * 1
            });
        me.nodeEnter.append("rect")
            .attr('class', 'plate')
            .attr({
                x: -me.boxWidth * 0.5,
                y: -me.boxHeight * 0,
                width: me.boxWidth * 1,
                height: me.boxHeight * 2,
            });

        me.nodeEnter.append("rect")
            .attr('class', 'frame')
            .attr({
                x: -me.boxWidth * 0.5,
                y: -me.boxHeight * 1,
                width: me.boxWidth * 1,
                height: me.boxHeight * 3,
            });
        me.nodeEnter.selectAll("rect.band")
            .attr('class', function(d) {
                return 'band ' + (d.ghost ? ' ghost' : '')+ (d.condition=='DEAD' ? ' dead' : '');
            });
        me.nodeEnter.selectAll("rect.frame")
            .attr('class', function(d) {
                return 'frame ' + (d.ghost ? ' ghost' : '')+ (d.condition=='DEAD' ? ' dead' : '');
            });
        me.nodeEnter.selectAll("rect.plate")
            .attr('class', function(d) {
                return 'plate ' + d.faction + (d.ghost ? ' ghost' : '')+ (d.condition=='DEAD' ? ' dead' : '');
            });

        // IMAGE
        me.nodeEnter.append("image")
            .attr("xlink:href", function(d) {
                let s;
                if (d.clan) {
                    s = 'static/collector/clans/' + d.clan.split(" ").join("_").toLowerCase() + '.webp';
                } else {
                    s = 'static/collector/' + "independant".split(" ").join("_").toLowerCase() + '.webp';
                }
                return s;
            })
            .attr('class', function(d) {
                return (d.ghost ? 'creature_img ghost' : 'creature_img');
            })
            .attr('id', function(d) {
                return d.id;
            })
            .attr("x", (-me.boxWidth * 0.70))
            .attr("y", (-me.boxHeight * 1.25))
            .attr("width", me.boxWidth * 0.30)
            .attr("height", me.boxHeight * 1)
            .on("click", function(d) {
                console.log("Just ctrl+clicked on image for " + d.id + " [" + d.name + "]!");
                if (d3.event.ctrlKey) {
                    toggleSimple(d);
                } else {
                    toggle(d);
                }
                me.update(d);

            });
        // TEXT
        me.nodeEnter.append("text")
            .attr('class', function(d) {
                let c = 'name';
                if (d.ghost) c += ' ghost';
                return c;
            })
            .append('tspan')
            .attr('text-anchor', 'start')
            .attr('x', -me.boxWidth * 0.3)
            .attr('y', -me.boxHeight * 0.5)
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
                let n = d.name;
                if (d.ghost) {
                    if (d.mythic){
                        n = d.name;
                    }
                    else{
                        n = 'Unknown';
                    }
                }
                return n;
            })
            .call(wrap, me.boxWidth * 0.7)
            .on("click", function(d) {
                if (d3.event.ctrlKey) {
                    console.log("Just ctrl+clicked on text for " + d.id + " [" + d.name + "]!");

                    $.ajax({
                        url: 'ajax/view/creature/' + d.rid + '/',
                        success: function(answer) {
                            $('.details').html(answer)
                            $('li').removeClass('selected');
                            $('.details').removeClass('hidden');
                            co.rebootlinks();
                        },
                        error: function(answer) {
                            console.log('View error...' + answer);
                        }
                    });
                }
            });

        // Display of the properties
        me.nodeEnter.selectAll("text")
            .append('tspan')
            .attr('class', 'property')
            .attr('text-anchor', 'start')
            .attr('x', -me.boxWidth * 0.45)
            .attr('y', me.boxHeight * 0.5)
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
                let str = '';
                if (d.ghost == false) {
                    if (d.clan) {
                        if (d.generation <= 3) {
                            str += d.clan + " Antediluvian"
                        } else {
                            str = d.generation + 'th gen.';
                            str += ' ' + d.clan;
                        }
                        str += " "+line_jump_code+' ' + d.faction;
                        if (d.condition != 'OK')
                            str += " "+line_jump_code+' ' + d.condition;
                        if (d.status != 'OK')
                            str += " "+line_jump_code+' ' + d.status;
                    }
                }
                return str
            })
            .call(wrap, me.boxWidth * 0.9);

        // *** NODE UPDATE ***
        me.nodeUpdate = me.node.transition()
            .duration(me.duration)
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            });
        me.nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // *** NODE EXIT ***
        me.nodeExit = me.node.exit().transition()
            .duration(me.duration)
            .attr("transform", function(d) {
                return "translate(" + me.source.x + "," + me.source.y + ")";
            })
            .remove();

        me.nodeExit.select('rect')
            .attr({
                x: 0,
                y: 0,
                width: 0,
                height: 0
            });
        me.nodeExit.select("text")
            .style("fill-opacity", 1e-6);

        // *** LINKS ***
        me.link = me.vis.selectAll("path.link")
            .data(me.tree.links(me.nodes), function(d) {
                return d.target.id;
            });

        me.link.enter().insert("svg:path", "g")
            .attr("class", function(d) {
                let c = 'link ';
                if ((d.target.ghost) || (d.target.parent.ghost)) {
                    c += ' ghost';
                }
                return c;
            })
            .attr("d", function(d) {
                let o = {
                    x: source.x0,
                    y: source.y0
                };
                return me.diagonal({
                    source: o,
                    target: o
                });
            })
            .transition()
            .duration(me.duration)
            .attr("d", me.diagonal);

        me.link.transition()
            .duration(me.duration)
            .attr("d", me.diagonal);

        me.link.exit().transition()
            .duration(me.duration)
            .attr("d", function(d) {
                let o = {
                    x: source.x,
                    y: source.y
                };
                return diagonal({
                    source: o,
                    target: o
                });
            })
            .remove();

        me.nodes.forEach(function(d) {
            d.x0 = d.x;
            d.y0 = d.y;
        });
    }

    perform() {
        let me = this;
        me.update(me.root);
    }

}
