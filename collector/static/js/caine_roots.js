/*
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      
*/
var treedata;
d3.json('static/js/kindred.json', function(error, treedata) {
    var root;
    var boxWidth = 180;
    var boxHeight = 50;
    var m = [10, 10, 10, 10],
        h = 1800 - m[1] - m[3],
        w = 900 - m[0] - m[2],
        i = 0,
        r = 2000,
        x = d3.scale.linear().domain([0, w]).range([0, w]),
        y = d3.scale.linear().domain([0, h]).range([0, h]);
    var vis = d3.select("#caine_roots").append("svg:svg")
        .attr("viewBox", "0 0 1200 900")
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2])
        .append("svg:g")
        .attr("transform", "translate(" + m[3] + "," + m[0] + ")")
        .call(d3.behavior.zoom().x(x).y(y).scaleExtent([1, 128]).on("zoom", zoom));

    vis.append("rect")
        .attr("class", "overlay")
        .attr("width", w + m[1] + m[3])
        .attr("height", h + m[0] + m[2])
        .attr("opacity", 0);

    var tree = d3.layout.tree()
        .size([h, w]);

    var diagonal = d3.svg.diagonal()
        .projection(function(d) {
            return [d.x, d.y];
        });

    root = treedata;
    root.x0 = 0;
    root.y0 = w / 2;

    function toggleAll(d) {
        if (d.children) {
            d.children.forEach(toggleAll);
            toggle(d);
        }
    };


    root.children.forEach(function(d){
      if (d.children){
        d.children.forEach(toggleAll);
      }
    });
    update(root);

    function update(source) {
        var duration = d3.event && d3.event.altKey ? 5000 : 500;
        var nodes = tree.nodes(root).reverse();
        nodes.forEach(function(d) {
            d.y = d.depth * 120;
        });

        var node = vis.selectAll("g.node")
            .data(nodes, function(d) {
                return d.id || (d.id = ++i);
            });

        // NODE ENTER
        var nodeEnter = node.enter().append("svg:g")
            .attr("class", "node")
            .attr("transform", function(d) {
                return "translate(" + source.x0 + "," + source.y0 + ")";
            })
            .on("click", function(d) {
                if (d3.event.ctrlKey){
                  toggleSimple(d);
                }else{
                  toggle(d);
                }
                update(d);
            });
        nodeEnter.append("rect")
            .attr('class','band')
            .attr({
                x: -boxWidth*0.55,
                y: -boxHeight/2,
                width: boxWidth*0.3,
                height: boxHeight
            });
        nodeEnter.append("rect")
            .attr('class','plate')
            .attr({
                x: -boxWidth*0.25,
                y: -boxHeight/2,
                width: boxWidth*0.75,
                height: boxHeight,
            })
            .style('fill','#303030');            
        nodeEnter.selectAll("rect")
            .attr('class',function(d){
              c = 'kindred '
              if (d.ghost){
                c += 'ghost'
              }else{
                c +=  d.faction;
              }
              return c;
              })
        nodeEnter.append("image")
          .attr("xlink:href", function(d) {
              if (d.clan){
              s = 'static/collector/clans/'+d.clan.split(" ").join("_").toLowerCase()+'.webp';
              console.log(s);
            }else{
              s = 'static/collector/'+"independant".split(" ").join("_").toLowerCase()+'.webp';
            }
              return s;
            })
          .attr("x", (-boxWidth*0.5)+"px")
          .attr("y", (-boxHeight*0.5)+"px")
          .attr("width", boxWidth*0.2+"px")
          .attr("height", boxHeight+"px");
        nodeEnter.append("text")
            .attr('class', function(d){
                c = 'name';
                if (d.ghost){
                  c += ' ghost';
                }
                return c;
              })
            .append('tspan')
            .attr('text-anchor', 'start')
            .attr('x', -boxWidth*0.2)
            .attr('y', '-1em')
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
                n = d.name;
                if (d.ghost){
                  n = 'unkown';
                }
                return n;
            });

            
        nodeEnter.selectAll("text")
            .append('tspan')
            .attr('class', function(d){
                c = 'property';
                if (d.ghost){
                  c += ' ghost';
                }
                return c;
              })
            .attr('text-anchor', 'start')
            .attr('x', -boxWidth*0.2)
            .attr('y', '0')
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
              if (d.ghost)
                str = '';
              else{
                str = d.generation+'th gen.';
                if (d.generation <= 3)
                  str = 'Antediluvian'
              }
                return str
            });
        nodeEnter.selectAll("text")
            .append('tspan')
            .attr('class', 'property')
            .attr('text-anchor', 'start')
            .attr('x', -boxWidth*0.2)
            .attr('y', '1em')
            .attr('dx', '0')
            .attr('dy', '0')
            .text(function(d) {
              str = '';
              if (d.ghost == false){
              if (d.clan){
                str = ""+d.clan;
              }
            }
              return str
            });

        // NODE UPDATE
        var nodeUpdate = node.transition()
            .duration(duration)
            .attr("transform", function(d) {
                return "translate(" + d.x + "," + d.y + ")";
            });
        nodeUpdate.select("text")
            .style("fill-opacity", 1);

        // NODE EXIT 
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

        var link = vis.selectAll("path.link")
            .data(tree.links(nodes), function(d) {
                return d.target.id;
            });

        link.enter().insert("svg:path", "g")
            .attr("class", "link")
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

    function transform(d) {
        return "translate(" + x(d.x) + "," + y(d.y) + ")";
    }

    function translate(d) {
      /*
        var sourceX = x(d.target.parent.y);
        var sourceY = y(d.target.parent.x);
        var targetX = x(d.target.y);
        var targetY = (sourceX + targetX) / 2;
        var linkTargetY = y(d.target.x0);
        var result = "M" + sourceX + "," + sourceY + " C" + targetX + "," + sourceY + " " + targetY + "," + y(d.target.x0) + " " + targetX + "," + linkTargetY + "";
      */
      
        var sourceX = x(d.target.parent.x);
        var sourceY = y(d.target.parent.y);
        var targetX = x(d.target.x);
        var targetY = y(d.target.y);
        var halfY = sourceY+(targetY-sourceY) / 2        
        var result = "M" + sourceX + "," + sourceY + " C" + sourceX + "," + halfY +" "+targetX+","+halfY+" "+targetX+","+targetY ;
        return result;
      
    }
});
