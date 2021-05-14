class CrossOverSheet{
    constructor(data,parent,collector) {
        let me = this;
        me.parent = parent;
        me.co = collector;
        me.config = data;
        me.init();
    }

    init(){
        let me = this;
        me.stepx = 40;
        me.stepy = 35;

        me.width = 24 * me.stepx;
        me.height = 36 * me.stepy;
        me.margin = [10,5,10,5];
        me.dot_radius = 6;
        me.stat_length = 150;
        me.stat_max = 5;
        me.draw_stroke = '#111';
        me.draw_fill = '#222';
        me.user_stroke = '#621';
        me.user_fill = '#B63';
        me.user_font = 'atma';
        me.title_font = 'Cinzel';
        me.logo_font = 'Trade Winds';
        me.base_font = 'Imprima';
        me.debug = false;
        me.pre_title = 'Willkommen zum';
        me.scenario = "Oktoberblutenfest";
        me.post_title = "Ein bayerisches Abenteuer"
        me.health_levels = ['Bruised/X','Hurt/-1','Injured/-1','Wounded/-2','Mauled/-2','Crippled/-5','Incapacitated/X'];
    }

    midline(y){
        let me = this;
        me.back.append('line')
            .attr('x1',me.stepx*2)
            .attr('x2',me.stepx*22)
            .attr('y1',me.stepy*y)
            .attr('y2',me.stepy*y)
            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")
            ;
    }

    drawWatermark(){
        let me = this;
        d3.select(me.parent).selectAll("svg").remove();
        me.svg = d3.select(me.parent).append("svg")
            .attr("id", me.data['rid'])
            .attr("viewBox", "0 0 2000 3000")
            .attr("x", 0)
            .attr("y", 0)
            .attr("width", me.width)
            .attr("height", me.height)
            ;

        //me.svg.append('style')


/*
            <style>
    @import url("https://fonts.googleapis.com/css2?family=Cinzel");
    @import url("https://fonts.googleapis.com/css2?family=Trade+Winds");
    @import url("https://fonts.googleapis.com/css2?family=Roboto");
    @import url("https://fonts.googleapis.com/css2?family=Imprima");
</style> \
*/

        me.back = me.svg
            .append("g")
            .attr("transform", "translate(" + 10 + "," + 17 + ") ")
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
            .style('stroke-width','0.5pt')
            .attr('opacity',1.0)
            ;

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
            .style('stroke-width','0.25pt')
           ;
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
            .style('stroke-width','0.25pt')
           ;
        }

        let decoration1 = me.back.append('g')
            .append('line')
            .attr('x1',me.stepx*1)
            .attr('y1',me.stepy*2)
            .attr('x2',me.stepx*1)
            .attr('y2',me.stepy*35)

            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")
            ;
        let decoration2 =  me.back.append('line')
            .attr('x1',me.stepx*23)
            .attr('x2',me.stepx*23)
            .attr('y1',me.stepy*2)
            .attr('y2',me.stepy*35)

            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")

            ;

        let decoration3 =  me.back.append('line')
            .attr('x1',me.stepx*5)
            .attr('y1',me.stepy*1)
            .attr('x2',me.stepx*19)
            .attr('y2',me.stepy*1)

            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")

            ;

        let decoration4 =  me.back.append('line')
            .attr('x1',me.stepx*1)
            .attr('x2',me.stepx*23)
            .attr('y1',me.stepy*35)
            .attr('y2',me.stepy*35)

            .style('fill','transparent')
            .style('stroke',me.draw_stroke)
            .style('stroke-width','3pt')
            .attr('marker-end', "url(#arrowhead)")
            .attr('marker-start', "url(#arrowhead)")

            ;

        me.midline(2);
        me.midline(8.5);
        me.midline(15);
        me.midline(21.5);
        me.midline(29);




        let decoration6_pre =  me.back.append('text')
            .attr("x",me.stepx*12)
            .attr("y",me.stepy*1.5)
            .attr("dy",0)
            .style("text-anchor",'middle')
            .style("font-family",me.logo_font)
            .style("font-size",'48px')
            .style("fill","#FFF")
            .style("stroke","#FFF")
            .style("stroke-width",'5pt')
            .text(me.scenario)
            .attr('opacity',1)
            ;



        let decoration5 =  me.back.append('text')
            .attr("x",me.stepx*1.5)
            .attr("y",me.stepy*1.75)
            .attr("dy",0)
            .style("text-anchor",'start')
            .style("font-family",me.base_font)
            .style("font-size",'16px')
            .style("fill",me.draw_fill)
            .style("stroke",me.draw_stroke)
            .style("stroke-width",'0.5pt')
            .text(me.pre_title)

            ;

        let decoration5bis =  me.back.append('text')
            .attr("x",me.stepx*22.5)
            .attr("y",me.stepy*1.75)
            .attr("dy",0)
            .style("text-anchor",'end')
            .style("font-family",me.base_font)
            .style("font-size",'16px')
            .style("fill",me.draw_fill)
            .style("stroke",me.draw_stroke)
            .style("stroke-width",'0.5pt')
            .text(me.post_title)

            ;



        let decoration6 =  me.back.append('text')
            .attr("x",me.stepx*12)
            .attr("y",me.stepy*1.5)
            .attr("dy",0)
            .style("text-anchor",'middle')
            .style("font-family",me.logo_font)
            .style("font-size",'48px')
            .style("fill","#000")
            .style("stroke","transparent")
            .style("stroke-width",'0.5pt')
            .text(me.scenario)
            .attr('opacity',1)
            ;

        let decoration6_line =  me.back.append('text')
            .attr("x",me.stepx*12)
            .attr("y",me.stepy*1.5)
            .attr("dy",0)
            .style("text-anchor",'middle')
            .style("font-family",me.logo_font)
            .style("font-size",'48px')
            .style("fill","transparent")
            .style("stroke","#A22")
            .style("stroke-width",'0.5pt')
            .text(me.scenario)
            .attr('opacity',1)
            ;


        let decoration8 =  me.back.append('text')
            .attr("x",me.stepx*1.5)
            .attr("y",me.stepy*35.8)
            .attr("dy",-16)
            .style("text-anchor",'start')
            .style("font-family",me.base_font)
            .style("font-size",'10px')
            .style("fill","#111")
            .style("stroke","#888")
            .style("stroke-width",'0.5pt')
            .text(me.guideline)
            .attr('opacity',1)
            ;
        let decoration9 =  me.back.append('text')
            .attr("x",me.stepx*22.5)
            .attr("y",me.stepy*35.2)
            .attr("dy",0)
            .style("text-anchor",'end')
            .style("font-family",me.base_font)
            .style("font-size",'8px')
            .style("fill","#111")
            .style("stroke","#888")
            .style("stroke-width",'0.5pt')
            .text("WaWWoD Cross+Over Sheet. (c) 2021, Pentex Inc.")
            .attr('opacity',1)
            ;



        me.character = me.back.append('g')
            .attr('class','xover_sheet');
    }

    reinHagenStat(name,value,ox,oy,type,statcode,source, power=false){
        let me = this;
        let item = source.append('g')
            .attr('class',type);
         item.append('rect')
             .attr('x',ox)
             .attr('y',oy)
             .attr('width',me.stat_length*1.6)
             .attr('height',18)
             .style('fill','#FFF')
             .style('stroke','transparent')
             .style('stroke-width','0.5pt')
             ;


        item.append('text')
            .attr("x",ox)
            .attr("y",oy)
            .attr("dy",12)
            .style("text-anchor",'start')
            .style("font-family",function(){
                return (power ? me.user_font : me.base_font);
                //return (power ? 'NothingYouCouldDo' : 'Titre');
            })
            .style("font-size",'12px')
            .style("fill",function(){
                return (power ? me.user_fill : me.draw_fill);
            })
            .style("stroke",function(){
                return (power ? me.user_stroke : me.draw_stroke);
            })
            .style("stroke-width",'0.5pt')
            .text(function(){
                return name.charAt(0).toUpperCase() + name.slice(1);
            })
        let max = me.stat_max;
        if (value>me.stat_max){
            max = me.stat_max*2;
        }

        let dots = item.append('g')
            .attr('class','dots '+type)
            .selectAll("g")
            .data(d3.range(0, max, 1));
        dots.enter()
            .append('circle')
            .attr('cx',function(d){
                let cx = ox+me.stepx*4+(d+1)*((me.dot_radius)*2);
                if (d>=me.stat_max){
                    cx = ox+me.stepx*4+(d+1-me.stat_max)*((me.dot_radius)*2);
                }
                return cx;
            })
            .attr('cy',function(d){
                let cy = oy+me.dot_radius/2+6;
                if (max > me.stat_max){
                    cy -=4;
                }

                if (d>=me.stat_max){
                    cy += +me.dot_radius/2+2;
                }
                return cy;
            })
            .attr('r',function(d){
                return  (d>=me.stat_max ? me.dot_radius-2:me.dot_radius-2);
            })
            .style('fill',function(d){
                return (d < value ? me.user_fill : "white");
            })
            .style('stroke',function(d){
                return me.draw_stroke;
            })
            .style('stroke-width','1pt')
           ;
    }

    powerStat(name,ox,oy,type,statcode,source){
        let me = this;
        if (name==''){
            me.reinHagenStat('   ',0,ox,oy,type,statcode,source)
        }else{
            let words = name.split(' (');
            let power = words[0];
            let val = (words[1].split(')'))[0];
            me.reinHagenStat(power,val,ox,oy,type,statcode,source,power=true)
        }
    }



    statText(name,value,ox,oy,type,statcode,source,fat=false){
        let me = this;
        let item = source.append('g')
            .attr('class',type);
         item.append('rect')
             .attr('x',ox)
             .attr('y',oy)
             .attr('width',me.stat_length*1.6)
             .attr('height',18)
             .style('fill','#FFF')
             .style('stroke','#FFF')
             .style('stroke-width','0.5pt')
             ;


        item.append('text')
            .attr("x",ox)
            .attr("y",oy)
            .attr("dy",10)
            .style("text-anchor",'start')
            .style("font-family",'Lato')
            .style("font-size",'12px')
            .style("fill",me.draw_fill)
            .style("stroke",me.draw_stroke)
            .style("stroke-width",'0.5pt')
            .text(function(){
                return name.charAt(0).toUpperCase() + name.slice(1);
            });

        if (fat){
        item.append('text')
            .attr("x",ox+me.stepx*2)
            .attr("y",oy)
            .attr("dy",12)
            .style("text-anchor",'start')
            .style("font-family",me.user_font)
            .style("font-size",'26px')
            .style("fill",me.user_fill)
            .style("stroke",me.user_stroke)
            .style("stroke-width",'0.5pt')
            .text(function(){
                return value;
            });
        }else{
        item.append('text')
            .attr("x",ox+me.stepx*2)
            .attr("y",oy)
            .attr("dy",12)
            .style("text-anchor",'start')
            .style("font-family",me.user_font)
            .style("font-size",'12px')
            .style("fill",me.user_fill)
            .style("stroke",me.user_stroke)
            .style("stroke-width",'0.5pt')
            .text(function(){
                return value;
            });
        }
    }

    title(name,ox,oy,source){
        let me = this;
        let item = source.append('g');
        item.append('text')
            .attr("x",ox)
            .attr("y",oy)
            .attr("dy",10)
            .style("text-anchor",'middle')
            .style("font-family",me.title_font)
            .style("font-size",'16px')
            .style("fill",'#111')
            .style("stroke",'#888')
            .style("stroke-width",'0.5pt')
            .text(function(){
                return name.charAt(0).toUpperCase() + name.slice(1);
            })

    }

    gaugeStat(name,value,ox,oy,source,withTemp=false,automax=false,max=10){
        let me = this;
        let type=name;
        let item = source.append('g');
        let lines = 1;
        let tempmax = max;

        item.append('text')
            .attr("x",ox)
            .attr("y",oy)
            .attr("dy",10)
            .style("text-anchor",'middle')
            .style("font-family",me.title_font)
            .style("font-size",'16px')
            .style("fill",'#111')
            .style("stroke",'#888')
            .style("stroke-width",'0.5pt')
            .text(function(){
                return name.charAt(0).toUpperCase() + name.slice(1);
            });
        if (automax){
            tempmax = (Math.round(value/10))*10;
            lines = tempmax/10;
        }

        let dots = item.append('g')
            .attr('class','dots '+type)
            .selectAll("g")
            .data(d3.range(0, tempmax, 1));
        let dot = dots.enter();
        dot.append('circle')
            .attr('cx',function(d){
                let cx =  ox+(d-((tempmax-1)/2))*((me.dot_radius+1)*2);
                if (d>=10){
                    cx = ox+((d-10)-4.5)*((me.dot_radius+1)*2);
                }
                return cx;
            })
            .attr('cy',function(d){
                let cy = oy+0.3*me.stepx+me.dot_radius;
                if (d>=10){
                    cy += me.dot_radius*2;
                }
                return cy;
            })
            .style('fill',function(d){
                return (d < value ? me.user_fill : "white");
            })
            .attr('r',me.dot_radius-2)
            .style('stroke',me.draw_stroke)
            .style('stroke-width','1pt')
            ;
        dot.append('rect')
            .attr('x',function(d){
                let cx =  ox+(d-4.5)*((me.dot_radius+1)*2) - me.dot_radius;
                if (d>=10){
                    cx = ox+((d-10)-4.5)*((me.dot_radius+1)*2) - me.dot_radius;
                }
                return cx;
            })
            .attr('y',function(d){
                let cy = oy+0.3*me.stepx+me.dot_radius - me.dot_radius + (me.dot_radius*2+2)*lines;
                if (d>=10){
                    cy += me.dot_radius*2+3 ;
                }
                return cy;
            })
            .attr('width',me.dot_radius*2)
            .attr('height',me.dot_radius*2)
            .style('fill',function(d){return (withTemp?'white':'transparent');})
            .style('stroke',function(d){return (withTemp?me.draw_stroke:'transparent');})
            .style('stroke-width','0.5pt')
           ;

    }


    fillAttributes(basey){
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = 'attribute';

        oy -= me.stepy;

        me.statText('Name',me.data['name'],ox+me.stepx*2,oy,'name','name',me.character,true);
        me.statText('Nature',me.data['nature'],ox+me.stepx*9,oy,'nature','nature',me.character);
        if (me.data["creature"]=='kindred'){
            me.statText('Age/R (Emb)',me.data['age']+"/"+me.data['trueage']+" ("+me.data['embrace']+"A.D)",ox+me.stepx*16,oy,'age','age',me.character);
        }else{
            me.statText('Age',me.data['age'],ox+me.stepx*16,oy,'age','age',me.character);
        }
        oy += 0.5*me.stepy;
        if (me.data['player']==''){
            me.statText('Position',me.data['position'],ox+me.stepx*2,oy,'player','player',me.character);
        }else{
            me.statText('Player',me.data['player'],ox+me.stepx*2,oy,'player','player',me.character);
        }
        me.statText('Demeanor',me.data['demeanor'],ox+me.stepx*9,oy,'demeanor','demeanor',me.character);
        me.statText('Sex',(me.data['sex']?'male':'female'),ox+me.stepx*16,oy,'sex','sex',me.character);

        oy += 0.5*me.stepy;
        me.statText('Chronicle',me.data['chronicle'],ox+me.stepx*2,oy,'chronicle','chronicle',me.character);
        me.statText('Residence',me.data['group'],ox+me.stepx*9,oy,'group','group',me.character);
        me.statText('Concept',me.data['concept'],ox+me.stepx*16,oy,'concept','concept',me.character);

        oy += 0.5*me.stepy;
        me.statText('Creature',me.data['creature'],ox+me.stepx*2,oy,'chronicle','chronicle',me.character);

        if (me.data["creature"]=='kindred'){
            me.statText('Cotterie',me.data['groupspec'],ox+me.stepx*9,oy,'group','group',me.character);
            me.statText('Clan',me.data['family'],ox+me.stepx*16,oy,'concept','concept',me.character);
        }else if (me.data["creature"]=='garou'){
            me.statText('Pack',me.data['groupspec'],ox+me.stepx*9,oy,'group','group',me.character);
            me.statText('Tribe',me.data['family'],ox+me.stepx*16,oy,'concept','concept',me.character);
        }


        oy += 1.5*me.stepy;

        me.title('Physical ('+me.data['total_physical']+')',ox+me.stepx*5,oy,me.character);
        me.title('Social ('+me.data['total_social']+')',ox+me.stepx*12,oy,me.character);
        me.title('Mental ('+me.data['total_mental']+')',ox+me.stepx*19,oy,me.character);

        oy += 0.5*me.stepy;
        ox = 2*me.stepx;
        [0,1,2,3,4,5,6,7,8].forEach(function(d) {
              let x = ox + me.stepx*7*((Math.round((d+2)/3))-1) ;
              let y = oy + 0.5*me.stepy*((d+3)%3);
              me.reinHagenStat(me.config['labels'][stat+'s'][d],me.data[stat+d],x,y,stat,stat+d,me.character);
        });

    }
    fillAbilities(basey){
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';

        me.title('Talents ('+me.data['total_talents']+')',ox+me.stepx*5,oy,me.character);
        me.title('Skills ('+me.data['total_skills']+')',ox+me.stepx*12,oy,me.character);
        me.title('Knowledges ('+me.data['total_knowledges']+')',ox+me.stepx*19,oy,me.character);

        oy += 0.5*me.stepy;

        stat = 'talent';
        [0,1,2,3,4,5,6,7,8,9].forEach(function(d) {
              let x = ox + me.stepx*2;
              let y = oy + 0.5*me.stepy*(d);
              me.reinHagenStat(me.config['labels'][stat+'s'][d],me.data[stat+d],x,y,stat,stat+d,me.character);
        });
        stat = 'skill';
        [0,1,2,3,4,5,6,7,8,9].forEach(function(d) {
              let x = ox + me.stepx*9;
              let y = oy + 0.5*me.stepy*(d);
              me.reinHagenStat(me.config['labels'][stat+'s'][d],me.data[stat+d],x,y,stat,stat+d,me.character);
        });
        stat = 'knowledge';
        [0,1,2,3,4,5,6,7,8,9].forEach(function(d) {
              let x = ox + me.stepx*16;
              let y = oy + 0.5*me.stepy*(d);
              me.reinHagenStat(me.config['labels'][stat+'s'][d],me.data[stat+d],x,y,stat,stat+d,me.character);
        });
    }

    fillAdvantages(basey){
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';

        me.title('Backgrounds ('+me.data['total_backgrounds']+')',ox+me.stepx*5,oy,me.character);
        if (me.data['creature']=='garou'){
            me.title('Gifts ('+me.data['total_gifts']+')',ox+me.stepx*12,oy,me.character);
            me.title('Renown',ox+me.stepx*19,oy,me.character);
        }else if (me.data['creature']=='kindred') {
            me.title('Disciplines ('+me.data['total_gifts']+')',ox+me.stepx*12,oy,me.character);
            me.title('Virtues',ox+me.stepx*19,oy,me.character);
        }else{
            me.title('Other Traits',ox+me.stepx*12,oy,me.character);
            me.title('Other Traits',ox+me.stepx*19,oy,me.character);
        }


        oy += 0.5*me.stepy;
        stat = 'background';
        [0,1,2,3,4,5,6,7,8,9].forEach(function(d) {
              let x = ox+me.stepx*2;
              let y = oy + 0.5*me.stepy*(d);
              me.reinHagenStat(me.config['labels'][stat+'s'][d],me.data[stat+d],x,y,stat,stat+d,me.character);
        });

        stat = 'gift';
        [0,1,2,3,4,5,6,7,8,9].forEach(function(d) {
              let x = ox+me.stepx*9;
              let y = oy + 0.5*me.stepy*(d);
              me.powerStat(me.data[stat+d],x,y,stat,stat+d,me.character);
        });

        stat = 'level';
        let levels = [];
        if (me.data['creature']=='garou') {
            levels = ['Glory','Honor','Wisdom'];
        }else{
            levels = ['Conscience','Self-Control','Courage'];
        }

        [0,1,2].forEach(function(d) {
              let x = ox+me.stepx*16;
              let y = oy + 0.5*me.stepy*(d);
              me.reinHagenStat(levels[d],me.data[stat+d],x,y,stat,stat+d,me.character);
        });

        if (me.data['creature']=='garou'){
            oy += 1.5*me.stepy;
            me.gaugeStat('Rank',me.data['rank'],ox+me.stepx*19,oy,me.character,false,false,5);
        }else if (me.data['creature']=='kindred'){

        }
    }


    drawHealth(basey){
        let me = this;
        let ox = 0;
        let oy = basey;
        me.title('Health',ox+me.stepx*19,oy,me.character);
        oy += me.stepy*0.8;
        let h = me.character.append('g')
            .selectAll('g')
            .data(me.health_levels)
        ;
        let x= h.enter();
            x.append('text')
            .attr('x',function(d,i){
                return ox+me.stepx*16;
            })
            .attr('y',function(d,i){
                return oy+i*me.stepy*0.6;
            })
            .style("text-anchor",'start')
            .style("font-family",me.base_font)
            .style("font-size",'12px')
            .style("fill",me.draw_fill)
            .style("stroke",me.draw_stroke)
            .style("stroke-width",'0.5pt')
            .text(function(d){
                let words = d.split('/');
                return words[0];
            });
            x.append('text')
            .attr('x',function(d,i){
                return ox+me.stepx*19;
            })
            .attr('y',function(d,i){
                return oy+i*me.stepy*0.6;
            })
            .style("text-anchor",'middle')
            .style("font-family",'Titre')
            .style("font-size",'12px')
            .style("fill",me.draw_fill)
            .style("stroke",me.draw_stroke)
            .style("stroke-width",'0.5pt')
            .text(function(d){
                let words = d.split('/');
                if (words[1]=='X'){
                    return '';
                }
                return words[1];
            });
        x.append('rect')
            .attr('x',function(d,i){
                return ox+me.stepx*21;
            })
            .attr('y',function(d,i){
                return oy+i*me.stepy*0.6-me.dot_radius*2;
            })
            .attr('width',me.dot_radius*2)
            .attr('height',me.dot_radius*2)
            .style("fill","white")
            .style("stroke",me.draw_stroke)
            .style("stroke-width",'0.5pt')
            ;

    }


    fillOther(basey){
        let me = this;
        let ox = 0;
        let oy = basey;
        let stat = '';


        me.title('Merits',ox+me.stepx*5,oy,me.character);


        oy += 0.5*me.stepy;
        stat = 'merit';
        [0,1,2,3,4].forEach(function(d) {
              let x = ox+me.stepx*2;
              let y = oy + 0.5*me.stepy*(d);
              me.powerStat(me.data[stat+d],x,y,stat,stat+d,me.character);
        });
        oy += 3*me.stepy;
        me.title('Flaws',ox+me.stepx*5,oy,me.character);
        oy += 0.5*me.stepy;
        stat = 'flaw';
        [0,1,2,3,4].forEach(function(d) {
              let x = ox + me.stepx*2;
              let y = oy + 0.5*me.stepy*(d);
              me.powerStat(me.data[stat+d],x,y,stat,stat+d,me.character);
        });

        oy = basey;
        me.gaugeStat('Willpower',me.data['willpower'],ox+me.stepx*12,oy,me.character,true);

        if (me.data['creature']=='garou'){
            oy += 1.7*me.stepy;
            me.gaugeStat('Rage',me.data['power1'],ox+me.stepx*12,oy,me.character,true);
            oy += 1.5*me.stepy;
            me.gaugeStat('Gnosis',me.data['power2'],ox+me.stepx*12,oy,me.character,true);
        }
        if (me.data['creature']=='kindred'){
            oy += 1.7*me.stepy;
            me.gaugeStat('Humanity',me.data['power1'],ox+me.stepx*12,oy,me.character);
            oy += 1.5*me.stepy;
            me.gaugeStat('Blood Pool',me.data['power2'],ox+me.stepx*12,oy,me.character,true,true);

        }
        oy = basey;
        me.drawHealth(oy);
    }

    fillCharacter(){
        let me = this;
        me.fillAttributes(4*me.stepy);
        me.fillAbilities(9*me.stepy);
        me.fillAdvantages(15.5*me.stepy);
        me.fillOther(22*me.stepy);

    }

  formatXml(xml) {
    var formatted = '';
    xml = xml.replace(/[\u00A0-\u2666]/g, function (c) {
      return '&#' + c.charCodeAt(0) + ';';
    })
    var reg = /(>)(<)(\/*)/g;
    xml = xml.replace(reg, '$1\r\n$2$3');
    var pad = 0;
    jQuery.each(xml.split('\r\n'), function (index, node) {
      var indent = 0;
      if (node.match(/.+<\/\w[^>]*>$/)) {
        indent = 0;
      } else if (node.match(/^<\/\w/)) {
        if (pad != 0) {
          pad -= 1;
        }
      } else if (node.match(/^<\w[^>]*[^\/]>.*$/)) {
        indent = 1;
      } else {
        indent = 0;
      }

      var padding = '';
      for (var i = 0; i < pad; i++) {
        padding += '  ';
      }

      formatted += padding + node + '\r\n';
      pad += indent;
    });

    return formatted;
  }


    drawButtons(){
        let me = this;
        let ox=0;
        let oy=3*me.stepy;
        let button = me.back.append('g')
            .attr('class','do_not_print')
        button.append('rect')
            .attr('x', ox-me.stepx*0.8)
            .attr('y', oy-0.4*me.stepy)
            .attr('width',me.stepx*1.6)
            .attr('height',me.stepy*0.8)
            .style('fill','#AAA')
            .style('stroke','#111')
            .style('stroke-width','1pt')
            .attr('opacity',1.0)
            .style('cursor','pointer')
            .on('click',function(d){
                me.saveSVG();
            })
            ;
        button.append('text')
            .attr('x', ox)
            .attr('y', oy)
            .attr('dy', 5)
            .style('font-family',me.base_font)
            .style('text-anchor','middle')
            .style('font-size','10pt')
            .style('fill','#000')
            .style('cursor','pointer')
            .style('stroke','#333')
            .style('stroke-width','0.5pt')
            .attr('opacity',1.0)
            .text('to SVG')
            .on('click',function(d){
                me.saveSVG();
            })
            ;

        button.append('rect')
            .attr('x', ox-me.stepx*0.8)
            .attr('y', oy-0.4*me.stepy+ me.stepy)
            .attr('width',me.stepx*1.6)
            .attr('height',me.stepy*0.8)
            .style('fill','#AAA')
            .style('stroke','#111')
            .style('stroke-width','1pt')
            .attr('opacity',1.0)
            .style('cursor','pointer')
            .on('click',function(d){
                me.savePDF();
            })
            ;
        button.append('text')
            .attr('x', ox)
            .attr('y', oy+me.stepy)
            .attr('dy', 5)
            .style('font-family',me.base_font)
            .style('text-anchor','middle')
            .style('font-size','10pt')
            .style('fill','#000')
            .style('cursor','pointer')
            .style('stroke','#333')
            .style('stroke-width','0.5pt')
            .attr('opacity',1.0)
            .text('to PNG')
            .on('click',function(d){
                me.savePDF();
            })

            ;
        button.append('rect')
            .attr('x', ox-me.stepx*0.8)
            .attr('y', oy-0.4*me.stepy+ 2*me.stepy)
            .attr('width',me.stepx*1.6)
            .attr('height',me.stepy*0.8)
            .style('fill','#AAA')
            .style('stroke','#111')
            .style('stroke-width','1pt')
            .attr('opacity',1.0)
            .style('cursor','pointer')
            .on('click',function(d){
                me.savePDF();
            })
            ;
        button.append('text')
            .attr('x', ox)
            .attr('y', oy+2*me.stepy)
            .attr('dy', 5)
            .style('font-family',me.base_font)
            .style('text-anchor','middle')
            .style('font-size','10pt')
            .style('fill','#000')
            .style('cursor','pointer')
            .style('stroke','#333')
            .style('stroke-width','0.5pt')
            .attr('opacity',1.0)
            .text('to PDF')
            .on('click',function(d){
                me.savePDF();
            })

            ;
        button.append('rect')
            .attr('x', ox-me.stepx*0.8)
            .attr('y', oy-0.4*me.stepy+ 3*me.stepy)
            .attr('width',me.stepx*1.6)
            .attr('height',me.stepy*0.8)
            .style('fill','#AAA')
            .style('stroke','#111')
            .style('stroke-width','1pt')
            .attr('opacity',1.0)
            .style('cursor','pointer')
            .on('click',function(d){
                me.editCreature();
            })
            ;
        button.append('text')
            .attr('x', ox)
            .attr('y', oy+3*me.stepy)
            .attr('dy', 5)
            .style('font-family',me.base_font)
            .style('text-anchor','middle')
            .style('font-size','10pt')
            .style('fill','#000')
            .style('cursor','pointer')
            .style('stroke','#333')
            .style('stroke-width','0.5pt')
            .attr('opacity',1.0)
            .text('UI details')
            .on('click',function(d){
                me.editCreature();
            })

            ;

    }

    savePDF(){
        let me = this;
        const doc = new jsPDF()
        const element = document.getElementById(me.data['rid'])
        doc.svg(element, {
            x,
            y,
            width,
            height
        }).then(() => {
            doc.save(me.data['rid']+'.pdf')
        })
    }


    savePNG(){
        let me = this;
        console.log("Save to PNG");

        me.svg.selectAll('.do_not_print').attr('opacity',0);
        // I recommend to keep the svg visible as a preview
        //let svg = $('#container > svg').get(0);


        // you should set the format dynamically, write [width, height] instead of 'a4'
        saveSvgAsPng(document.getElementById(me.data['rid']), me.data['rid']+".png");
        me.svg.selectAll('.do_not_print').attr('opacity',1);
    }

    saveSVG(){
        let me = this;
        me.svg.selectAll('.do_not_print').attr('opacity',0);
        let base_svg = d3.select("svg").html();
        let exportable_svg = '<?xml version="1.0" encoding="ISO-8859-1" ?> \
<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd"> \
<svg class="crossover_sheet" \
xmlns="http://www.w3.org/2000/svg" version="1.1" \
xmlns:xlink="http://www.w3.org/1999/xlink"> \
' + base_svg + '</svg>';
        let fname = me.data['rid']+ ".svg"
        let nuke = document.createElement("a");
        nuke.href = 'data:application/octet-stream;base64,' + btoa(me.formatXml(exportable_svg));
        nuke.setAttribute("download", fname);
        nuke.click();
        me.svg.selectAll('.do_not_print').attr('opacity',1);
    }

    editCreature(){
        $('.details').removeClass('hidden');
    }


    perform(character_data){
        let me = this;
        me.data = character_data;
        me.guideline = me.data['guideline']
        me.drawWatermark();
        me.fillCharacter();
        me.drawButtons();
    }
}

