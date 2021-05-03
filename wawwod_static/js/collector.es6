class WawwodCollector {
    constructor() {
        console.log('Starting ')
        this.d3 = undefined;
        this.init();
    }

    init() {
        let me = this;
        me.prepare_ajax();
    }

    prepare_ajax() {
        $.ajaxSetup({
            beforeSend: function (xhr, settings) {
                if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
                    let csrf_middlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
                    xhr.setRequestHeader('X-CSRFToken', csrf_middlewaretoken);
                }
            }
        });
    }

    loadAjax() {
        let me = this;
        $('.charlist').addClass('hidden');
//         $.ajax({
//             url: 'ajax/list/1/',
//             success: function (answer) {
//                 $('.charlist').addClass('hidden');
//                 $('.charlist').html(answer.list)
//                 $('.more').addClass('hidden');
//                 $('.details').addClass('hidden');
//                 //me.updateGaiaWheel();
//                 me.rebootLinks();
//             },
//         });
    }

    updateLineage(){
        $('#toggle_lineage').off();
        $('#toggle_lineage').on('click', function (event) {
            $.ajax({
                url: 'ajax/display/lineage',
                success: function (answer) {

                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error('Lineage Error');
                    me.rebootLinks();
                },

            });
        });
    }

//     updateGaiaWheel() {
//         let me = this;
//         $.ajax({
//             url: 'ajax/display/gaia_wheel/',
//             success: function (answer) {
//                 $('#custom_js').html(answer.gaia_wheel);
//             },
//             error: function (answer) {
//                 console.error('Gaia Wheel Error');
//                 me.rebootLinks();
//             },
//         });
//     }

    registerDisplay(){
        let me = this;
        $('.display').off().on('click', function (event) {
            let slug = $(this).attr('id');
            $.ajax({
                url: 'ajax/display/' + slug + '/',
                success: function (answer) {
                    console.log('Display '+slug);
                    let d = JSON.parse(answer.data);
                    console.log(d);
                    me.d3 = new GaiaWheel(d,"#d3area",me);
                    me.d3.perform();
                    //$('#d3area').html(answer.run);
                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error(answer);
                    me.rebootLinks();
                },
            });
        });

    }


    registerSwitch(){
        let me = this;
        $('.switch').off().on('click', function (event) {
            let slug = $(this).attr('id');
            $.ajax({
                url: 'ajax/switch/chronicle/' + slug + '/',
                success: function (answer) {
                    console.log('switch');
                    $('#chronicle_menu').html(answer.chronicles);
                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error(answer);
                    me.rebootLinks();
                },
            });
        });

    }

    registerList(){
        let me = this;
        $('.list').off().on('click', function (event) {
            let slug = $(this).attr('id');
            $.ajax({
                url: 'ajax/list/creatures/1/' + slug + '/',
                success: function (answer) {
                    console.log('list');
                    $('.charlist').attr('title',slug);
                    $('.charlist').html(answer.list);
                    $('.more').addClass('hidden');
                    $('.charlist').removeClass('hidden');
                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error(answer);
                    me.rebootLinks();
                },
            });
        });

    }

    registerNav(){
        let me = this;
        $('.nav').off().on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let key = $('#customize').val();
            let slug = $('.charlist').attr('title');
            if (key == '') {
                key = 'none';
            }
            $.ajax({
                url: 'ajax/list/creatures/' + $(this).attr('page') + '/'+slug+'/',
                success: function (answer) {
                    $('.charlist').html(answer.list);

                    me.rebootLinks();
                    $('.more').addClass('hidden');
                },
            });
        });


    }


    rebootLinks() {
        let me=this;
        me.registerSwitch();
        me.registerList();
        me.registerNav();
        me.registerDisplay();




        $('#go').off();
        $('#go').on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let urlupdate = 'ajax/update/character/' + $('.character_form input[name=id]').val();
            $.ajax({
                url: urlupdate,
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                data: {
                    cid: $('.character_form input[name=cid]').val(),
                    character: $('.character_form').serialize(),
                },
                dataType: 'json',
                success: function (answer) {
                    $('.details').html(answer.character);
                    $('li#' + answer.rid).html(answer.line);
                    $('li').find('div.avatar_link').removeClass('selected');
                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error('Error... ' + answer);
                },
            });
        });

        $('.toggle_more').off();
        $('.toggle_more').on('click', function (event) {
            event.preventDefault();
            $('.more').addClass('hidden');
            zid = $(this).attr('id');
            x = zid.split("_");
            $('.more#m_' + x[1]).toggleClass('hidden');
            me.rebootLinks();
        });




//         $('#toggle_list').off();
//         $('#toggle_list').on('click', function (event) {
//             $('.charlist').toggleClass('hidden');
//         });

        $('#toggle_details').off();
        $('#toggle_details').on('click', function (event) {
            $('.details').toggleClass('hidden');
        });

        $('#toggle_details2').off();
        $('#toggle_details2').on('click', function (event) {
            $('.details').toggleClass('hidden');
        });


        $('#build_config_pdf').off();
        $('#build_config_pdf').on('click', function (event) {
            event.preventDefault();
            $.ajax({
                url: 'ajax/build_config_pdf/',
            }).done(function (answer) {
                $('.details').html(answer.comment);
                me.rebootLinks();
            });
        });

        $('.view_creature').off();
        $('.view_creature').on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let dad = $(this).parents('li');
            $('li').removeClass('selected');
            $(dad).addClass('selected');
            $.ajax({
                url: 'ajax/view/creature/' + $(this).attr('id') + '/',
                success: function (answer) {
                    $('.details').html(answer)
                    $('li').removeClass('selected');
                    $('.details').removeClass('hidden');
                    me.rebootLinks();
                },
                error: function (answer) {
                    console.error('View error...' + answer);
                }
            });
        });

        $('td.editable.userinput').off();
        $('td.editable.userinput').hover(
            function (event) {
                $(this).addClass('focus');
                $('#userinput').focus();
                me.rebootLinks();
            },
            function (event) {
                $(this).removeClass('focus');
                me.rebootLinks();
            });

        $('td.editable.updown').off();
        $('td.editable.updown').hover(
            function (event) {
                $(this).addClass('focus');
                me.rebootLinks();
            },
            function (event) {
                $(this).removeClass('focus');
                me.rebootLinks();
            });
        $('td.editable.updown').on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let target = $(this).attr('id')
            let keys = $(this).attr('id').split('_')
            let shift = event.shiftKey
            let block = $(this).parent();
            let os = 1;
            if (shift) {
                os = -1;
            }
            let keys_set = {id: keys[0], field: keys[1], offset: os}
            $.ajax({
                url: 'ajax/editable/updown',
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                dataType: 'json',
                data: keys_set,
                success: function (answer) {
                    $('td#' + target).html(answer.new_value);
                    $('td#' + keys[0] + '_freebies').html(answer.freebies);
                },
                error: function (answer) {
                    $('td#' + target).html(answer.new_value);
                },
            });
        });

        $('td.editable.userinput').on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let target = $(this).attr('id')
            let keys = $(this).attr('id').split('_')
            let shift = event.shiftKey;
            let val = $('#userinput').val();
            let block = $(this).parent();
            if (shift) {
                let keys_set = {id: keys[0], field: keys[1], value: val}
                $.ajax({
                    url: 'ajax/editable/userinput',
                    method: 'POST',
                    headers: {
                        'Accept': 'application/json',
                        'Content-Type': 'application/x-www-form-urlencoded'
                    },
                    dataType: 'json',
                    data: keys_set,
                    success: function (answer) {
                        $('td#' + target).html(answer.new_value);
                        $('td#' + keys[0] + '_freebies').html(answer.freebies);
                    },
                    error: function (answer) {
                        $('td#' + target).html(answer);
                    },
                });
            }
        });


        $('#add_creature').off().on('click', function (event) {
            event.preventDefault();
            event.stopPropagation();
            let val = $('#userinput').val();
            let keys_set = {creature: val}
            $.ajax({
                url: 'ajax/add/creature/',
                method: 'POST',
                headers: {
                    'Accept': 'application/json',
                    'Content-Type': 'application/x-www-form-urlencoded'
                },
                dataType: 'json',
                data: keys_set,
                success: function (answer) {
                    $('.details').html(answer)
                    $('#userinput').val("");
                    rebootLinks();
                },
                error: function (answer) {
                    $('.details').html('oops, broken')
                    rebootLinks();
                },

            });
        });


    }


    perform() {
        let me = this;
        me.loadAjax();
        me.rebootLinks();
    }

}


















