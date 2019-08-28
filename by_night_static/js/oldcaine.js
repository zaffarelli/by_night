


var root;

var boxWidth = 150,
    boxHeight = 40,
    duration = 750;

var zoom = d3.behavior.zoom()
  .scaleExtent([.1,1])
  .on('zoom', function(){
    svg.attr("transform", "translate(" + d3.event.translate + ") scale(" + d3.event.scale + ")");
  })
  .translate([150, 200]);

var svg = d3.select("#caine_roots").append("svg")
  .attr('width', 1000)
  .attr('height', 500)
  .call(zoom)
  .append('g')
  .attr("transform", "translate(150,200)");

var tree = d3.layout.tree()
  .nodeSize([100, 200])
  .separation(function(){
    return .5;
  })
  .children(function(person){
    if(person.collapsed){
      return;
    } else {
      return person.children;
    }
  });

d3.json('static/js/kindred.json', function(error, json){ 
  if(error) {
    return console.error(error);
  }
  json.children.forEach(collapse);
  /*
  json.children.forEach(function(gen2){
    gen2.children.forEach(function(gen3){
      collapse(gen3);
    });
  });
  * */
  root = json;
  root.x0 = 0;
  root.y0 = 0;
  draw(root);
});

function draw(source){
  var nodes = tree.nodes(root),
      links = tree.links(nodes);
  var link = svg.selectAll("path.link")
      .data(links, function(d){ return d.target.id; });
  link.enter().append("path")
      .attr("class", "link")
      .attr("d", function(d) {
        var o = {x: source.x0, y: (source.y0 + boxWidth*3/2)};
        return transitionElbow({source: o, target: o});
      });
  link.transition()
      .duration(duration)
      .attr("d", elbow);
  link.exit()
      .transition()
      .duration(duration)
      .attr("d", function(d) {
        var o = {x: source.x, y: (source.y + boxWidth/2)};
        return transitionElbow({source: o, target: o});
      })
      .remove();
  var node = svg.selectAll("g.person")
      .data(nodes, function(person){ return person.id; });
  var nodeEnter = node.enter().append("g")
      .attr("class", "person")
      .attr('transform', function(person){
        return 'translate(' + (source.y0 + boxWidth/2) + ',' + source.x0 + ')';
      })
      .on('click', togglePerson);
  nodeEnter.append("rect")
      .attr({
        x: 0,
        y: 0,
        width: 0,
        height: 0
      });
  nodes.filter(function(d,i){
    return d.status == "myth";
  }).append('rect')
  .attr('class', 'myth');      
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

  nodeUpdate.select('text')
      .attr("dx", -(boxWidth/2) + 10)
      .style('fill-opacity', 1);
  var nodeExit = node.exit()
      .transition()
      .duration(duration)
      .attr("transform", function(d) { return "translate(" + (source.y + boxWidth/2) + "," + source.x + ")"; })
      .remove();
  nodeExit.select('rect')
      .attr({
        x: 0,
        y: 0,
        width: 0,
        height: 0
      });
  nodeExit.select('text')
      .style('fill-opacity', 0)
      .attr('dx', 0);
  nodes.forEach(function(person) {
    person.x0 = person.x;
    person.y0 = person.y;
  });
}

function togglePerson(person){  
  if(person.collapsed){
    person.collapsed = false;
    console.log(person.name+' collapsed');
  } else {
    console.log(person.name+' not collapsed');
    collapse(person);
  }
  draw(person);
}

function collapse(person){
  person.collapsed = true;
  console.log(person.name+' is collapsing');
  if(person.children){
    console.log(person.name+': collapsing children');  
    person.children.forEach(collapse);
  }
}
    
function elbow(d) {
  var sourceX = d.source.x,
      sourceY = d.source.y + (boxWidth / 2),
      targetX = d.target.x,
      targetY = d.target.y - (boxWidth / 2);
      
  return "M" + sourceY + "," + sourceX
    + "H" + (sourceY + (targetY-sourceY)/2)
    + "V" + targetX 
    + "H" + targetY;
}

function transitionElbow(d){
  return "M" + d.source.y + "," + d.source.x
    + "H" + d.source.y
    + "V" + d.source.x 
    + "H" + d.source.y;
}
