/*
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      
*/





var treedata = {
   "name":"Caine",
   "clan":"Kindred",
   "generation":1,
   "children":[
      {
         "name":"Enoch the Wise",
         "generation":2,
         "children":[
            {
               "name":"Arikel",
               "generation":3,
               "clan":"Toreador",
               "children":[

               ]
            },
            {
               "name":"Malkav",
               "generation":3,
               "clan":"Malkavian",
               "children":[

               ]
            },
            {
               "name":"Saulot",
               "generation":3,
               "clan":"Salubri",
               "children":[
                  {
                     "name":"Tremere",
                     "generation":4,
                     "clan":"Tremere",
                     "children":[

                     ]
                  }
               ]
            },
            {
               "name":"Ennoia",
               "generation":3,
               "clan":"Gangel",
               "children":[

               ]
            }
         ]
      },
      {
         "name":"Irad the Strong",
         "generation":2,
         "children":[
            {
               "name":"Ventru",
               "generation":3,
               "clan":"Ventrue",
               "children":[
               {
                  "name":"Meneleus",
                  "generation":4,
                  "clan":"Ventrue",
                  "children":[
                    {
                      "name":"Marius Flavius Vespasianus",
                      "generation":5,
                      "clan":"Ventrue",
                      "children":[]
                    }
                  ]
               },
               {
                  "name":"Mithras",
                  "generation":4,
                  "clan":"Ventrue",
                  "children":[
                    {
                      "name":"Marcus Verus",
                      "generation":5,
                      "clan":"Ventrue",
                      "children":[
                        {
                          "name":"Peter Van der Waals",
                          "generation":6,
                          "clan":"Ventrue",
                          "children":[
                          ]
                        }
                      ]
                    }
                  ]
               }               

               ]
            },
            {
               "name":"Brujah",
               "generation":3,
               "clan":"True Brujah",
               "children":[
                  {
                     "name":"Troile",
                     "generation":4,
                     "clan":"Brujah",
                     "children":[

                     ]
                  }
               ]
            },
            {
               "name":"Cappadocius",
               "generation":3,
               "clan":"Cappadocian",
               "children":[
                  {
                     "name":"Augustus Giovanni",
                     "generation":4,
                     "clan":"Giovanni",
                     "children":[

                     ]
                  }
               ]
            },
            {
               "name":"Lasombra",
               "clan":"Lasombra",
               "generation":3,
               "children":[

               ]
            },
            {
               "name":"The Eldest",
               "clan":"Tzimisce",
               "generation":3,
               "children":[

               ]
            }
         ]
      },
      {
         "name":"Zillah the Beautiful",
         "generation":2,
         "children":[
            {
               "name":"Absimiliard",
               "clan":"Nosferatu",
               "generation":3,
               "children":[

               ]
            },
            {
               "name":"Set",
               "generation":3,
               "clan":"Setite",
               "children":[

               ]
            },
            {
               "name":"Haqim",
               "clan":"Assamite",
               "generation":3,
               "children":[

               ]
            }
         ]
      }
   ]
};

var boxWidth = 170;
var boxHeight = 45;
var m = [20, 20, 20, 20],
    w = 1200 - m[1] - m[3],
    h = 800 - m[0] - m[2],
    i = 0,
    r = 1200,
    x = d3.scale.linear().domain([0, w]).range([0, w]),
    y = d3.scale.linear().domain([0, h]).range([0, h]),
    root;
var vis = d3.select("#caine_roots").append("svg:svg")
    .attr("viewBox", "0 0 600 600")
    .attr("width", w + m[1] + m[3])
    .attr("height", h + m[0] + m[2])
    .append("svg:g")
    .attr("transform", "translate(" + m[3] + "," + m[0] + ")")
    .call(d3.behavior.zoom().x(x).y(y).scaleExtent([1,8]).on("zoom",zoom));

    vis.append("rect")
      .attr("class", "overlay")
      .attr("width", w + m[1] + m[3])
      .attr("height", h + m[0] + m[2])
      .attr("opacity", 0);

var tree = d3.layout.tree()
      .size([h, w]);

var diagonal = d3.svg.diagonal()
      .projection(function(d) { return [d.y, d.x]; });

    root = treedata;
    root.x0 = h / 2;
    root.y0 = 0;

function toggleAll(d) {
  if (d.children) {
    d.children.forEach(toggleAll);
    toggle(d);
  }
};

root.children.forEach(toggleAll);
update(root);

function update(source) {
  var duration = d3.event && d3.event.altKey ? 5000: 500;
  var nodes = tree.nodes(root).reverse();
  nodes.forEach(function (d) {
    d.y = d.depth * 300;
});

var node = vis.selectAll("g.node")
    .data(nodes, function(d) { return d.id || (d.id = ++i); });
var nodeEnter = node.enter().append("svg:g")
    .attr("class", "node")
    .attr("transform", function(d) {return "translate(" + source.y0 + "," + source.x0 + ")"; })
    .on("click", function(d) {
        toggle(d);
        update(d);
        if (d['info']) {
            playvid(d['info']);
        }
    });
nodeEnter.append("rect")
    .attr({
      x: 0,
      y: 0,
      width: 0,
      height: 0
    });
nodeEnter.append("text")
    .attr('class', 'name')
    .append('tspan')      
    .attr('text-anchor', 'start')
    .attr('x',-boxWidth/2)
    .attr('y',0)
    .attr('dx',4)
    .attr('dy',-2)
    .text(function(d) { 
      return d.name;
    });      
nodeEnter.selectAll("text")
    .append('tspan')
    .attr('class', 'property')      
    .attr('text-anchor', 'start')
    .attr('x',-boxWidth/2)
    .attr('y','1em')
    .attr('dx',4)
    .attr('dy',1)
    .text(function(d) { 
      return d.clan+' generation '+d.generation; 
    });
var nodeUpdate = node.transition()
    .duration(duration)
    .attr("transform", function(d) { return "translate(" + d.y + "," + d.x + ")"; });
nodeUpdate.select('rect')
    .attr({
      x: -(boxWidth/2),
      y: -(boxHeight/2),
      width: boxWidth,
      height: boxHeight
    });
  nodeUpdate.select("text")
    .style("fill-opacity", 1);

/* NODE EXIT */
var nodeExit = node.exit().transition()
  .duration(duration)
  .attr("transform", function(d) { return "translate(" + source.y + "," + source.x + ")"; })
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
  .data(tree.links(nodes), function(d) { return d.target.id; });

link.enter().insert("svg:path", "g")
    .attr("class", "link")
    .attr("d", function(d) {
      var o = {x: source.x0, y: source.y0};
      return diagonal({source: o, target: o});
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
    var o = {x: source.x, y: source.y};
    return diagonal({source: o, target: o});
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
  }
  else {
    //closeSiblings(d);
    d.children = d._children;
    d._children = null;
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
  return "translate(" + x(d.y) + "," + y(d.x) + ")";
}

function translate(d) {
  var sourceX = x(d.target.parent.y);
  var sourceY = y(d.target.parent.x);
  var targetX = x(d.target.y);
  var targetY = (sourceX + targetX)/2;
  var linkTargetY = y(d.target.x0);
  var result = "M"+sourceX+","+sourceY+" C"+targetX+","+sourceY+" "+targetY+","+y(d.target.x0)+" "+targetX+","+linkTargetY+"";
  return result;
}

























