class Storytelling{
    constructor(data,parent,collector) {
        let me = this;
        me.parent = parent;
        me.co = collector;
        me.config = data;
        me.init();
    }

    decorationText(x,y,d=0,a='middle',f,s,b,c,w,t,v,o=1){
        let me = this;
        v.append('text')
            .attr("x",me.stepx*x)
            .attr("y",me.stepy*y)
            .attr("dy",d)
            .style("text-anchor",a)
            .style("font-family",f)
            .style("font-size",s+'px')
            .style("fill",b)
            .style("stroke",c)
            .style("stroke-width",w+'pt')
            .text(t)
            .attr('opacity',o);
    }


    midline(y,startx=2,stopx=22){
        let me = this;
        me.back.append('line')
            .attr('x1',me.stepx*startx)
            .attr('x2',me.stepx*stopx)
            .attr('y1',me.stepy*y)
            .attr('y2',me.stepy*y)
            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")
            ;
    }

    crossline(x,starty=2,stopy=35){
        let me = this;
        me.back.append('line')
            .attr('x1',me.stepx*x)
            .attr('x2',me.stepx*x)
            .attr('y1',me.stepy*starty)
            .attr('y2',me.stepy*stopy)
            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")
            ;
    }


  init(){
        let me = this;
        me.debug = true;
        me.stretch_coeff = 2;
        me.width = parseInt($(me.parent).css("width"),10) * 1;
        me.height = me.width *1.41  *me.stretch_coeff ; // 0.707 paysage
        me.w = 1.25 * me.width;
        me.h = 1.25 * me.height;
        me.stepx = me.width/24;
        me.stepy = me.height/(36*me.stretch_coeff);
        me.scene_dim = me.stepy / 3;
        me.tiny_font_size = me.stepy / 5;
        me.small_font_size = 1.3*me.stepy / 5;
        me.medium_font_size = 2*me.stepy / 5;
        me.large_font_size = 2.5*me.stepy / 5;
        me.fat_font_size = 8*me.stepy / 5;
        me.margin = [0,0,0,0];
        me.dot_radius = me.stepx/8;
        me.stat_length = 150;
        me.stat_max = 5;
        me.shadow_fill = "#B0B0B0";
        me.shadow_stroke = "#A0A0A0";
        me.draw_stroke = '#111';
        me.draw_fill = '#222';
        me.user_stroke = '#911';
        me.user_fill = '#A22';
        me.user_font = 'Gochi Hand';
        me.mono_font = 'Syne Mono';
        me.title_font = 'Khand';
        me.logo_font = 'Trade Winds';
        //me.logo_font = 'Reggae One';
        me.base_font = 'Philosopher';
        me.x = d3.scale.linear().domain([0, me.width]).range([0, me.width]);
        me.y = d3.scale.linear().domain([0, me.height]).range([0, me.height]);
        me.pre_title = me.config['pre_title'];
        me.scenario = me.config['scenario'];
        me.post_title = me.config['post_title'];
        me.health_levels = ['Bruised/X','Hurt/-1','Injured/-1','Wounded/-2','Mauled/-2','Crippled/-5','Incapacitated/X'];
        me.d_start_x = me.stepx*3
        me.d_start_y = me.stepy*5;
        me.p_start_x = me.stepx*4;
        me.p_start_y = me.stepy*4;
    }

    drawWatermark(){
        let me = this;
        d3.select(me.parent).selectAll("svg").remove();
        me.svg = d3.select(me.parent).append("svg")
            .attr("id", me.data['rid'])
            .attr("viewBox", "0 0 " + me.w + " " + me.h)
            .attr("width", me.width)
            .attr("height", me.height)
            .append("svg:g")
            .attr("transform", "translate(0,0)")
            .call(d3.behavior.zoom().x(me.x).y(me.y).scaleExtent([2, 8]).on("zoom", function(e){
                })
            );
        me.back = me.svg
            .append("g")
            .attr("class", "page")
            .attr("transform", "translate("+0*me.stepx+","+0*me.stepy+")")
            ;
        me.defs = me.svg.append('defs');
        me.defs.append('marker')
            .attr('id', 'arrowhead')
            .attr('viewBox', '-0 -5 10 10')
            .attr('refX', 0)
            .attr('refY', 0)
            .attr('orient', 'auto-start-reverse')
            .attr('markerWidth', 9)
            .attr('markerHeight', 9)
            .attr('preserveAspectRatio', 'xMidYMid meet')
            .attr('xoverflow', 'visible')

            .append('svg:path')
                    .attr('d', 'M 1,-1 l 3,1 -3,1 -1,-1 1,-1 M 5,-1 l  3,1 -3,1 -1,-1 1,-1   Z')
                .style('fill', me.draw_fill)
                .style('stroke', me.draw_stroke)
                .style('stroke-width', '0pt')
            ;
        me.back.append('rect')
            .attr('x',0)
            .attr('y',0)
            .attr('width',me.width)
            .attr('height',me.height)
            .style('fill','white')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','0')
            .attr('opacity',1.0)
            ;
        // Grid
        if (me.debug){
            let verticals = me.back.append('g')
                .attr('class','verticals')
                .selectAll("g")
                .data(d3.range(0, 24, 1));
            verticals.enter()
                .append('line')
                .attr('x1',function(d){ return d*me.stepx})
                .attr('y1',0)
                .attr('x2',function(d){ return d*me.stepx})
                .attr('y2',36*me.stepy)
                .style('fill','transparent')
                .style('stroke','#CCC')
                .style('stroke-width','0.25pt');
            let horizontals = me.back.append('g')
                .attr('class','horizontals')
                .selectAll("g")
                .data(d3.range(0, 36, 1));
            horizontals.enter()
                .append('line')
                .attr('x1',0)
                .attr('x2',24*me.stepx)
                .attr('y1',function(d){ return d*me.stepy})
                .attr('y2',function(d){ return d*me.stepy})
                .style('fill','transparent')
                .style('stroke','#CCC')
                .style('stroke-width','0.25pt');
        }

        let days_count = (me.end_time / 24) +1;


        let days = me.back.append('g')
            .attr('class','days')
            .selectAll("g")
            .data(d3.range(0, days_count, 1));
        let day_in = days.enter()
        day_in.append('rect')
                .attr('class','day_rect')
                .attr('x', function(d){
                    return me.d_start_x + 0;
                })
                .attr('y', function(d){
                    return me.d_start_y + d*(me.stepy*(3+1));
                })
                .attr('width',function(d){
                    return me.stepx*17;
                })
                .attr('height',function(d){
                    return me.stepy*3;
                })
                .style('fill','#080')
                .style('stroke','transparent')
                .style('stroke-width','0.25pt')
                .attr('opacity','0.2')
                ;
        day_in.append('text')
                .attr('class','day_txt')
                .attr('x', function(d){
                    return me.d_start_x - 5;
                })
                .attr('y', function(d){
                    return me.d_start_y + d*(me.stepy*(3+1));
                })
                .attr('dy', 20)
                .style("text-anchor",'end')
                .style("font-family",me.base_font)
                .style("font-size",me.small_font_size+'px')
                .style("fill",me.draw_fill)
                .style("stroke",me.draw_stroke)
                .style("stroke-width",'0.5pt')
                .text(function(d){return "Day #"+d})
           ;


        let places = me.back.append('g')
            .attr('class','places')
            .selectAll("g")
            .data(me.places);
        let place_in = places.enter();
        place_in.append('rect')
            .attr('class','place_rect')
            .attr('x', function(d,i){
                return me.p_start_x + i*(me.stepx*(3+1));
            })
            .attr('y', function(d){
                return me.p_start_y + 0;
            })
            .attr('width',function(d){
                return me.stepx*3;
            })
            .attr('height',function(d){
                return me.stepy*29;
            })
            .style('fill','#008')
            .style('stroke','transparent')
            .style('stroke-width','0.25pt')
            .attr('opacity','0.1')
           ;
        place_in.append('text')
                .attr('class','place_txt')
                .attr('x', function(d,i){
                    return me.p_start_x + i*(me.stepx*(3+1));
                })
                .attr('y', function(d){
                    return me.p_start_y + 0;
                })
                .attr('dy', -40)
                .style("text-anchor",'start')
                .style("font-family",me.base_font)
                .style("font-size",me.small_font_size+'px')
                .style("fill",me.draw_fill)
                .style("stroke",me.draw_stroke)
                .style("stroke-width",'0.5pt')
                .text(function(d){return d['acronym']+" ("+d['id']+")";})
           ;
        place_in.append('text')
                .attr('class','place_txt')
                .attr('x', function(d,i){
                    return me.p_start_x + i*(me.stepx*(3+1));
                })
                .attr('y', function(d){
                    return me.p_start_y + 0;
                })
                .attr('dy', -20)
                .style("text-anchor",'start')
                .style("font-family",me.base_font)
                .style("font-size",me.tiny_font_size+'px')
                .style("fill",me.draw_fill)
                .style("stroke",me.draw_stroke)
                .style("stroke-width",'0.5pt')
                .text(function(d){return d['name'];})
           ;



        let lines = me.back.append('g');
        me.crossline(1,2,35);
        me.crossline(23,2,35);
        // Mid lines
//         me.midline(1.5,5,19);
        me.midline(2.5,1,23);
        me.midline(35,1,23);

//         me.midline(6);
//         me.midline(9);
//         me.midline(16);
//         me.midline(23);
//         me.midline(30);
        // Title
        //let txt = me.sheet_type(me.data['creature']).toUpperCase();
//         me.decorationText(12,2.75,0,'middle',me.title_font,me.fat_font_size*2,'#FFF','#FFF',10,txt,me.back,1);
//         me.decorationText(12,1.8,0,'middle',me.logo_font,me.fat_font_size,"#fff","#fff",5,me.scenario,me.back,0.75);

//         me.decorationText(12,1.8,0,'middle',me.logo_font,me.fat_font_size,me.shadow_fill,me.shadow_stroke,0.5,me.scenario,me.back,0.5);
//         me.decorationText(12,2.75,0,'middle',me.title_font,me.fat_font_size*2,me.shadow_fill,me.shadow_stroke,1,txt,me.back,0.75);

        //me.decorationText(12,1.8,0,'middle',me.logo_font,me.fat_font_size,"transparent",me.draw_stroke,0.5,me.scenario,me.back,0.5);

        me.decorationText(1.25,1.75,0,'start',me.title_font,me.large_font_size,me.draw_fill,me.draw_stroke,0.5,"Story: "+me.story['name'],me.back);
        me.decorationText(22.75,1.75,0,'end',me.title_font,me.large_font_size,me.draw_fill,me.draw_stroke,0.5,"Chronicle: "+me.story['chronicle_id'],me.back);



        // Sheet content
        me.story_map = me.back.append('g')
            .attr('class','storytelling');
    }

    drawStory(){
        let me=this;
        let scenes = me.story_map.append('g')
            .attr('class','scenes')
            .selectAll("g")
            .data(me.scenes);
        let scene_in = scenes.enter()
        scene_in.append("rect")
            .attr('x',function(d,i){
                return me.d_start_x + me.stepx;
            })
            .attr('y',function(d,i){
                return me.p_start_y + me.stepy + (d['time']/24 ) * me.stepy*(3+1);
            })
            .attr('width',me.scene_dim)
            .attr('height',me.scene_dim)
            .style('fill','#fff')
            .style('stroke','#000')
            .style('stroke-width','0.5pt')
            .attr('opacity',1.0)
            ;
    }

    perform(data){
        let me=this;
        me.data = data;
        me.story = JSON.parse(data['story']);
        me.places = JSON.parse(data['places']);
        me.scenes = JSON.parse(data['scenes']);
        me.end_time = JSON.parse(data['end_time'])
        console.log(me.data);
        me.drawWatermark()
        me.drawStory()
    }

 }