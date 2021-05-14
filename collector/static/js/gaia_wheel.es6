/*
    WaWWoD
*/
/* The Gaia wheel display class */
class GaiaWheel {
    constructor(data,parent,collector) {
        let me = this;
        me.parent = parent;
        me.co = collector;
        me.data = data;
        me.init();
    }

    init() {
        let me = this;
        me.global_rotation=0;
        me.sector_size = 60;
        me.weaver = me.data['weaver'];
        me.wyld = me.data['wyld'];
        me.wyrm = me.data['wyrm'];
        me.boxWidth = 6;
        me.boxHeight = 4;
        let re = new RegExp("\d+");
        me.width = parseInt($(me.parent).css("width"),10);
        me.height = me.width;
        me.radius = 800;
        me.max_gauge = 20;
        me.scales_stroke = "#989";
        me.scales_stroke_special = "#656";
        me.base_dash = "18 6";
        me.radiused = d3.scale.linear().domain([0, me.max_gauge]).range([150, me.radius]);
        me.unradiused = d3.scale.linear().domain([150,me.radius]).range([0, me.max_gauge]);
    }

    watermark(){
        let me = this;
        d3.select(me.parent).selectAll("svg").remove();
        me.svg = d3.select(me.parent).append("svg")
            //.attr("viewBox", "0 0 " + me.width + " " + me.height)
            .attr("width", me.width)
            .attr("height", me.height)
            ;

        me.back = me.svg
            .append("g")
            .attr("transform", "translate(" + me.width/2 + "," + me.height/2 + ") rotate("+(me.global_rotation)+")")
            ;
        //me.draw_sectors();
        let radial_lines = me.svg.append("g")
            .attr("class", "radiuses")
            .selectAll("g")
            .data(d3.range(0, 360, 10))
            ;
        radial_lines.enter()
            .append("g")
            .attr("transform", function (d) {
                return "translate(" + (me.width / 2) + "," + (me.height /2) + ") rotate(" + (d) + ")";
            })
            .append("line")
            .style("stroke", function(d){
                let res = me.scales_stroke;
                if ( (d-me.global_rotation) % me.sector_size == 0){
                    res = me.scales_stroke_special;
                }
                return res;
            } )
            .style("stroke-dasharray", function(d){
                let res = me.base_dash;
                if ( (d-me.global_rotation) % me.sector_size == 0){
                    res = "";
                }
                return res;
            } )
            .style("stroke-width",  function(d){
                let res = "0.25pt";
                if ( (d-me.global_rotation) % me.sector_size == 0){
                    res = "1pt";
                }
                return res;
            } )
            .attr("x1", me.radiused(0))
            .attr("x2", me.radiused(me.max_gauge))
            ;
        radial_lines.exit()
            .remove()
            ;

        me.inner_circles = me.back.append("g")
            .attr("class", "angulars")
            .selectAll("g")
            .data(d3.range(0, me.max_gauge+1, 1));
        me.inner_circles.enter()
            .append('circle')
            .attr("cx",0)
            .attr("cy",0)
            .attr("r",function(d){
                return me.radiused(d)
            })
            .style("fill",'transparent')
            .style("stroke",function(d){
                let res = me.scales_stroke;
                if (d % 5 == 0){
                    res = me.scales_stroke_special;
                }
                return res;
            })
            .style("stroke-dasharray",function(d){
                let res = me.base_dash;
                if (d % 5 == 0){
                    res = '';
                }
                return res;
            })
            .style("stroke-width",function(d){
                let res = '0.5pt';
                if (d % 5 == 0){
                    res = '1pt';
                }
                return res;
            })
            ;
        me.inner_circles.exit()
            .remove()
            ;
        me.tooltip = d3.select("body").append("div")
            .attr("class", "tooltip")
            .style("opacity", 0.5);
        me.cross = me.back.append('path')
            .attr("d","M 0 10 v -20 M 10 0 h -20 Z")
            .style("fill",'transparent')
            .style("stroke",me.scales_stroke)
            .style("stroke-width",'5pt')
            .on("click",function(e){
                let x = 10;
                if (d3.event.ctrlKey) {
                    me.global_rotation += x;
                }else{
                    me.global_rotation -= x;
                }
                me.perform();
            })
            ;
        }


    display_branch(angle,arr,ty,total, span){
        let me = this;
        let poles = {}
        arr.forEach(function(d,idx) {
              d.order = idx;
              d.angular = ((d.order+1)*span/(total+2))+angle*me.sector_size;
              d.radial = me.radiused(d.display_gauge);
              d.x = Math.cos((d.angular)*2*Math.PI/360) * d.radial;
              d.y = Math.sin((d.angular)*2*Math.PI/360) * d.radial;
              if (d.display_pole != ''){
                if (poles[d.display_pole]){
                    poles[d.display_pole]['count'] += 1;
                    poles[d.display_pole]['list'].push({'name':d.name, 'x':d.x, 'y':d.y, 'angular':d.angular, 'radial':d.radial, 'display_gauge': d.display_gauge});
                }else{
                    poles[d.display_pole] = {'count':1, 'list': [{'name':d.name, 'x':d.x, 'y':d.y, 'angular':d.angular, 'radial':d.radial, 'display_gauge': d.display_gauge}] };
                }
              }
        });
        //console.log(poles);
        let all_poles = []
        let links = [];
        for (let pole in poles) {
            let cx = 0;
            let cy = 0;
            let cnt = poles[pole]['list'].length;
            poles[pole]['list'].forEach(function(v,k){
                cx += v.x + Math.cos((v.angular)*2*Math.PI/360)*50;
                cy += v.y + Math.sin((v.angular)*2*Math.PI/360)*50;
            });

            poles[pole]['center'] = {'x':Math.round(cx/cnt),'y':Math.round(cy/cnt)};
            all_poles.push({'name':pole,'x':Math.round(cx/cnt),'y':Math.round(cy/cnt)})
        }
        for (let pole in poles) {
            let first = poles[pole]['list'][0];
            let previous = first;
            let center = poles[pole]['center'];
            poles[pole]['list'].forEach(function(v,k){
                links.push({'x1':v.x,'y1':v.y,'x2':center.x,'y2':center.y})
            });
        }
        let pole_centers = me.back.selectAll(".pole_center_"+ty)
            .data(all_poles)
        ;
        let pole_center = pole_centers.enter()
            .append("rect")
            .attr("class",'pole_center_'+ty)
            .attr("x",function(d){
                return d.x -5 ;
            })
            .attr("y",function(d){
                return d.y - 5;
            })
            .attr("width",10)
            .attr("height",10)
            .style('stroke','#111')
            .style('stroke-width','1pt')
            .style('fill','#FC4')
            .attr('opacity',0.5)

            ;


        let links_lines = me.back.selectAll(".link_line_"+ty)
            .data(links)
        ;
        let link = links_lines.enter()
            .append("line")
            .attr("class","link_line_"+ty)
            .attr("x1",function(d){
                return d.x1;
            })
            .attr("y1",function(d){
                return d.y1;
            })
            .attr("x2",function(d){
                return d.x2;
            })
            .attr("y2",function(d){
                return d.y2;
            })
            .style('stroke','#222')
            .style('stroke-width','1pt')
            .style('stroke-dasharray','7 3')
            .style('fill','transparent')
            .attr('opacity',0.5)
        ;


        let nodes = me.back.selectAll("."+ty)
            .data(arr)
        ;
        let node_cross = nodes.enter()
            .append("svg:g")
                .attr("transform", function(d) {
                    let trans = "";
                    trans += "translate("+d.x+","+ d.y +") ";
                    return trans;
                })
                .attr("class", "creature_view "+ty)
                .attr("id", function(d){
                    return d.id;
                })
                .attr("character", function(d){
                    return d.name;
                })
                .attr("creature", function(d){
                    return d.creature;
                })
            .on("mouseover", function(d) {
                  let breeds = ['Homid','Metis','Lupus'];
                  let auspices = ['Ragabash','Theurge','Philodox','Galliard','Ahroun'];
                  let str = ''
                  str += "<strong>"+d.name+"</strong>";
                    if (d.creature == 'garou'){
                        str += "<br/><i>Rank "+d.rank;
                        str += " "+breeds[d.breed];
                        str += " "+auspices[d.auspice];
                        str += " "+d.family+"</i>";
                    }
                    str += "<br/> (" + d.display_pole+ ", " + d.display_gauge + ")";
                    str += "<br/>["+d.position+"]";
                    str += "<br/>["+d.rid+"]";
                  me.tooltip.transition()
                    .duration(200)
                    .style("opacity", 1.0);
                  me.tooltip.html(str)
                    .style("left", Math.round(me.width/2-75) + "px")
                    .style("top", Math.round(me.height/2-30) + "px");
            })
            .on("mouseout", function(d) {
                me.tooltip.transition()
                .duration(1000)
                .style("opacity", 0);
            })
            .on("click", function(d) {
                if (d3.event.ctrlKey) {
                    $.ajax({
                        url: 'ajax/view/creature/' + d.rid + '/',
                        success: function(answer) {
                            $('.details').html(answer)
                            $('li').removeClass('selected');
                            $('.details').removeClass('hidden');
                            me.co.rebootLinks();
                        },
                        error: function(answer) {
                            console.error('View error...' + answer);
                        }
                    });
                }

            })
            ;


        node_cross.append('path')
            .attr("transform","rotate("+(-me.global_rotation)+")")
            .attr("d",function(d){
                return "M 0 10 v -20 M 10 0 h -20 "
            })
            .style("fill",'transparent')
            .style("stroke",'#000')
            .style("stroke-width",'1pt')
            ;
        node_cross.append('text')
            .attr("transform","rotate("+(-me.global_rotation)+")")
            .attr("dy",'-12px')
            .style("text-anchor",'middle')
            .style("font-family",'Lato')
            .style("font-size",'8pt')
            .style("fill",'#111')
            .style("stroke",'#888')
            .style("stroke-width",'0.5pt')
            .text(function(d){
                let name = '';
                let words = d.name.split(' ');
                words.forEach(function(word,k){
                    name += word[0];
                })
                return name;//+" ("+d.order+" / "+(Math.round(d.angular*100)/100)+")";
            })
            ;
        node_cross.append("circle")
            .attr('class', function(d){
                let res = 'node_circle '+ty+' '+d.creature;
                if (d.status == 'OK'){
                    res += ' balanced';
                }
                return res;
               })
            .attr({
                cx: 0,
                cy: 0,
            })
            .attr('r',function(d){
                let res = me.boxWidth;
                return res;
            })

            .style('opacity','0.8')
            ;
        let node_off = nodes.exit()
            .remove();
    }

  draw_sectors() {
    let me = this;
    me.position = me.radius*0.65;
    let data = [
        {'id':0,'start':0,'end':me.sector_size*2,'name':  'The Wyld','font':'wyld','angle':70*me.sector_size*0},
        {'id':1,'start':me.sector_size*2,'end':me.sector_size*3,'name':'The Weaver','font':'weaver','angle':70+me.sector_size*2},
        {'id':2,'start':me.sector_size*3,'end':me.sector_size*4,'name':'The Wyrm','font':'wyrm','angle':70+me.sector_size*3}
    ];
    let sectors = me.back.append("g")
      .attr("class", 'sectors')
      .selectAll(".sectors")
      .data(data);
    sectors.enter()
      .append("g")
      .attr("class", "sector")
      .attr("transform", function (d) {
        let x = Math.cos((d.angle)*2*Math.PI/360)*me.position;
        let y = Math.sin((d.angle)*2*Math.PI/360)*me.position;
        return "translate("+x+","+y+") ";
      })
      .append("text")
      .attr("transform","rotate("+(-me.global_rotation)+")")
      .attr("class", "category_name")
      .style("font-family", function(d){
        return d.font;
      })
      .style("font-size", "60pt")
      .style("text-anchor", "middle")
      .style("fill", "#666")
      .style("stroke", "#AAA")
      .style("opacity", "0.75")
      .text(function (d) {
        return d.name;
      });
    sectors.exit().remove();
  }


    update() {
        let me = this;
        me.display_branch(0,me.wyld,"wyld",me.wyld.length, me.sector_size*4);
        me.display_branch(4,me.weaver,"weaver",me.weaver.length, me.sector_size);
        me.display_branch(5,me.wyrm,"wyrm",me.wyrm.length,  me.sector_size);
    }

    perform() {
        let me = this;
        me.watermark()
        me.update();
    }
}
