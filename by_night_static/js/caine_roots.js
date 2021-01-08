/*
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      
*/
var treedata;
   
d3.json('static/js/kindred.json',function(error, treedata) {
    var root;
    var boxWidth = 120;
    var boxHeight = 140;
    var m = [0, 0, 0, 0],
        fw = 2048,
        fh = 2048,
        h = fh - m[1] - m[3],
        w = fw - m[0] - m[2],
        i = 0,
        x = d3.scale.linear().domain([0, w]).range([0, w]),
        y = d3.scale.linear().domain([0, h]).range([0, h]);
    var vis = d3.select("#caine_roots").append("svg:svg")
        .attr("viewBox", "0 0 "+fh+" "+fw)
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2])
        .append("svg:g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")")
        .call(d3.behavior.zoom().x(x).y(y).scaleExtent([0.125,4]).on("zoom", zoom));

    vis.append("rect")
        .attr("class", "overlay")
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2]);

    var tree = d3.layout.cluster()
        .size([fh,fw]);

    var diagonal = d3.svg.diagonal()
        .projection(function(d) {
            return [d.x, d.y];
        });

    root = treedata;
    root.x0 = 0;
    root.y0 = 0;

    function toggleAll(d) {
        if (d.children) {
            d.children.forEach(toggleAll);
            toggle(d);
        }
    };


    root.children.forEach(function(d) {
        if (d.children) {
          d.children.forEach(toggleAll)
        }
    });
    update(root);

    function update(source) {
        var duration = d3.event && d3.event.altKey ? 5000 : 500;
        var nodes = tree.nodes(root).reverse();
        nodes.forEach(function(d) {            
            d.y = d.depth * boxHeight*1.5;
        });

        var node = vis.selectAll("g.node")
            .data(nodes, function(d) {
                return d.id || (d.id = ++i);
            });

        // *** NODE ENTER ***
        // SHAPES
        var nodeEnter = node.enter().append("svg:g")
            .attr("class", "node")
            .attr("transform", function(d) {
                return "translate(" + source.x0 + "," + source.y0 + ")";
            });

        nodeEnter.append("rect")
            .attr('class', 'band')
            .attr({
                x: -boxWidth*0.5,
                y: -boxHeight*0.55,
                width: boxWidth*1,
                height: boxHeight*0.3
            });
        nodeEnter.append("rect")
            .attr('class', 'plate')
            .attr({
                x: -boxWidth*0.5,
                y: -boxHeight*0.25,
                width: boxWidth * 1,
                height: boxHeight*0.5,
            });
            
        nodeEnter.append("rect")
            .attr('class', 'frame')
            .attr({
                x: -boxWidth*0.5,
                y: -boxHeight*0.55,
                width: boxWidth * 1,
                height: boxHeight*0.8,
            });
        nodeEnter.selectAll("rect.band")
            .attr('class', function(d) {
              return 'band '+(d.ghost?' ghost':'');
            });
        nodeEnter.selectAll("rect.frame")
            .attr('class', function(d) {
              return 'frame '+(d.ghost?' ghost':'');
            });
        nodeEnter.selectAll("rect.plate")
            .attr('class', function(d) {
              return 'plate '+d.faction+(d.ghost?' ghost':'');
            });
           
        // IMAGE 
        nodeEnter.append("image")
            .attr("xlink:href", function(d) {
                if (d.clan) {
                    s = 'static/collector/clans/' + d.clan.split(" ").join("_").toLowerCase() + '.webp';
                    console.log(s);
                } else {
                    s = 'static/collector/' + "independant".split(" ").join("_").toLowerCase() + '.webp';
                }
                return s;
            })
            .attr('class', function(d) {
                return (d.ghost ? 'creature_img ghost': 'creature_img');
            })
            .attr('id', function(d) {
                return d.id;
            })
            .attr("x", (-boxWidth * 0.7) )
            .attr("y", (-boxHeight * 0.6) )
            .attr("width", boxWidth * 0.30 )
            .attr("height", boxHeight*0.30 )
            .on("click", function(d) {
              if (d3.event.ctrlKey) {
                      toggleSimple(d);
                  } else {
                      toggle(d);
                  }
                  update(d);
 
            });
        // TEXT 
        nodeEnter.append("text")
            .attr('class', function(d) {
                c = 'name';
                if (d.ghost) c += ' ghost';
                return c;
            })
            .append('tspan')
            .attr('text-anchor', 'start')
            .attr('x', -boxWidth * 0.3)
            .attr('y', -boxHeight*0.4)
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
                n = d.name;
                if (d.ghost) {
                    n = 'unkown';
                }
                return n;
            })
            .call(wrap,boxWidth*0.7)
            .on("click", function(d) {
                if (d3.event.ctrlKey) {
                console.log("Just ctrl+clicked on "+d.id+" ["+d.name+"]!");
                  
                $.ajax({      
                  url: 'ajax/view/creature/'+d.id+'/',
                  success: function(answer) {
                    $('.details').html(answer)
                    $('li').removeClass('selected');
                    $('.details').removeClass('hidden');
                    rebootlinks();
                  },
                  error: function(answer){
                    console.log('View error...'+answer);
                  }
                });
              }
            });

        // Display of the properties
        nodeEnter.selectAll("text")
            .append('tspan')
            .attr('class', 'property')
            .attr('text-anchor', 'start')
            .attr('x', -boxWidth*0.45)
            .attr('y', -boxHeight*0.10)
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
                str = '';
                if (d.ghost == false) {
                    if (d.clan) {
                        if (d.generation <= 3) {
                            str += d.clan + " Antediluvian"
                        } else {
                            str = d.generation + 'th gen.';
                            str += " " + d.clan;
                        }
                        str += ' '+d.faction;
                    }
                }
                return str
            })
            .call(wrap, boxWidth*0.9);

        // *** NODE UPDATE ***
        var nodeUpdate = node.transition()
            .duration(duration)
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            });
        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // *** NODE EXIT ***
        var nodeExit = node.exit().transition()
            .duration(duration)
            .attr("transform", function(d) {
                return "translate(" + source.x + "," + source.y + ")";
            })
            .remove();

        nodeExit.select('rect')
            .attr({
                x: 0,
                y: 0,
                width: 0,
                height: 0
            });
        nodeExit.select("text")
            .style("fill-opacity", 1e-6);

        // *** LINKS ***
        var link = vis.selectAll("path.link")
            .data(tree.links(nodes), function(d) {
                return d.target.id;
            });

        link.enter().insert("svg:path", "g")
            .attr("class", function(d){
              c = 'link ';
              if ((d.target.ghost)||(d.target.parent.ghost)){
                c += ' ghost';
              }
              return c;
              })
            .attr("d", function(d) {
                var o = {
                    x: source.x0,
                    y: source.y0
                };
                return diagonal({
                    source: o,
                    target: o
                });
            })
            .transition()
            .duration(duration)
            .attr("d", diagonal);

        link.transition()
            .duration(duration)
            .attr("d", diagonal);

        link.exit().transition()
            .duration(duration)
            .attr("d", function(d) {
                var o = {
                    x: source.x,
                    y: source.y
                };
                return diagonal({
                    source: o,
                    target: o
                });
            })
            .remove();

        nodes.forEach(function(d) {
            d.x0 = d.x;
            d.y0 = d.y;
        });
    }


    // Toggle functions
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


    function zoom(d) {
        var nodes = vis.selectAll("g.node");
        nodes.attr("transform", transform);
        var link = vis.selectAll("path.link");
        link.attr("d", translate);
    }
    
/*
   function zoom(d) {
        var scale = d3.event.scale,
            translation = d3.event.translate,
            tbound = -h * scale * 100,
            bbound = h * scale,
            lbound = (-w + m[3]) * scale,
            rbound = (w - m[1]) * scale;
        console.log("pre min/max" + translation);
        // limit translation to thresholds
        translation = [
        Math.max(Math.min(translation[0], rbound), lbound),
        Math.max(Math.min(translation[1], bbound), tbound)];
        console.log("scale" + scale);
        console.log("translation" + translation);
        d3.select("g")
            .attr("transform", "translate(" + translation + ")" +
            " scale(" + scale + ")");

    }
    */

    function transform(d) {
        return "translate(" + x(d.x) + "," + y(d.y) + ")";
    }

    // Links translation
    function translate(d) {      
        var result = '';
        var sourceX = x(d.target.parent.x);
        var sourceY = y(d.target.parent.y);
        var targetX = x(d.target.x);
        var targetY = y(d.target.y);
        var halfY = sourceY + (targetY - sourceY) / 2
        result = "M" + sourceX + "," + sourceY + " C" + sourceX + "," + halfY + " " + targetX + "," + halfY + " " + targetX + "," + targetY;
        return result;

    }

    // Word Wrap
    function wrap(text, width) {
        text.each(function() {
            var text = d3.select(this),
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
        });
    }


});


