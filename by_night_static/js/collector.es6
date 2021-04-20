/*
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      
*/
function prepare_ajax(){
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        let csrf_middlewaretoken = $('input[name=csrfmiddlewaretoken]').val();
        xhr.setRequestHeader('X-CSRFToken',csrf_middlewaretoken);
      }
    }
  });
}
 
function loadajax(){
  $.ajax({
    url: 'ajax/list/1/',
    success: function(answer) {            
      $('.charlist').html(answer.list)
      rebootlinks();
      $('.more').addClass('hidden');
      $('.charlist').addClass('hidden');
      $('.details').addClass('hidden');
    },
  });
}

function rebootlinks(){
  $('.nav').off();
  $('.nav').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    key = $('#customize').val(); 
    if (key == ''){
      key='none';
    }
    $.ajax({
      url: 'ajax/list/'+$(this).attr('page')+'/',
      success: function(answer) {
        $('.charlist').html(answer.list);
        $('#gaia_wheel').html(answer.gaia_wheel);
        rebootlinks();
        $('.more').addClass('hidden');
      },
    });   
  });


  $('#go').off();
  $('#go').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    let urlupdate = 'ajax/update/character/'+$('.character_form input[name=id]').val();
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
      success: function(answer) {
          $('.details').html(answer.character);          
          $('li#'+answer.rid).html(answer.line);
          $('li').find('div.avatar_link').removeClass('selected');
          rebootlinks();
      },
      error: function(answer) {
        console.error('Error... '+answer);
      },
    });  
  });

  $('.toggle_more').off();
  $('.toggle_more').on('click',function(event){
    event.preventDefault();
    $('.more').addClass('hidden');
    zid = $(this).attr('id');
    x = zid.split("_");
    $('.more#m_'+x[1]).toggleClass('hidden');
    rebootlinks();
  });

    $('#toggle_chronicle').off().on('click',function(event){
        let slug = $('#userinput').val();
        $.ajax({
            url: 'ajax/chronicle/'+slug+'/',
                success: function(answer) {
                rebootlinks();
            },
            error: function(answer) {
                //$('.details').html('oops, broken')
                console.error(answer);
                rebootlinks();
            },
        });
    });



  $('#toggle_lineage').off();
  $('#toggle_lineage').on('click',function(event){
    $.ajax({
      url: 'ajax/update/lineage',
      success: function(answer) {
        rebootlinks();
      },
      error: function(answer) {
        rebootlinks();
      },

    });
  });

  $('#toggle_list').off();
  $('#toggle_list').on('click',function(event){
    $('.charlist').toggleClass('hidden');
  });

  $('#toggle_details').off();
  $('#toggle_details').on('click',function(event){
    $('.details').toggleClass('hidden');
  });

  $('#toggle_details2').off();
  $('#toggle_details2').on('click',function(event){
    $('.details').toggleClass('hidden');
  });




  $('#build_config_pdf').off();
  $('#build_config_pdf').on('click',function(event){
    event.preventDefault();
    $.ajax({
      url: 'ajax/build_config_pdf/',
    }).done(function(answer) {
        $('.details').html(answer.comment);
        rebootlinks();
    });
  });

  $('.view_creature').off();
  $('.view_creature').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    let dad = $(this).parents('li');
    $('li').removeClass('selected');
    $(dad).addClass('selected');
    $.ajax({      
      url: 'ajax/view/creature/'+$(this).attr('id')+'/',
      success: function(answer) {
        $('.details').html(answer)
        $('li').removeClass('selected');
        $('.details').removeClass('hidden');
        rebootlinks();
      },
      error: function(answer){
        console.error('View error...'+answer);
      }
    });
  });

  $('td.editable.userinput').off();
  $('td.editable.userinput').hover(
    function(event){
      $(this).addClass('focus');
      $('#userinput').focus();
      rebootlinks();
      },
    function(event){
      $(this).removeClass('focus');
      rebootlinks();
      });
      
  $('td.editable.updown').off();
  $('td.editable.updown').hover(
    function(event){
      $(this).addClass('focus');
      rebootlinks();
      },
    function(event){
      $(this).removeClass('focus');
      rebootlinks();
      });
  $('td.editable.updown').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    let target = $(this).attr('id')
    let keys = $(this).attr('id').split('_')
    let shift = event.shiftKey
    let block = $(this).parent();
    let os = 1;
    if (shift){
      os = -1;
    }
    keys_set = { id: keys[0], field: keys[1], offset: os}
    $.ajax({
      url: 'ajax/editable/updown',
      method: 'POST',
      headers: {
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded'
      },
      dataType:'json',
      data: keys_set,      
      success: function(answer) {
        $('td#'+target).html(answer.new_value);
        $('td#'+keys[0]+'_freebies').html(answer.freebies);
          },
        error: function(answer){
            $('td#'+target).html(answer.new_value);
        },
      });
    });

  $('td.editable.userinput').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    let target = $(this).attr('id')
    let keys = $(this).attr('id').split('_')
    let shift = event.shiftKey;
    let val = $('#userinput').val();
    let block = $(this).parent();
    if (shift){
      keys_set = { id: keys[0], field: keys[1], value: val}
      $.ajax({
        url: 'ajax/editable/userinput',
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        dataType:'json',
        data: keys_set,      
        success: function(answer) {
            $('td#'+target).html(answer.new_value);
            $('td#'+keys[0]+'_freebies').html(answer.freebies);
          },
        error: function(answer){
            $('td#'+target).html(answer);
        },
      });
    }
  });


  $('#add_creature').off().on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    let val = $('#userinput').val();
    let keys_set = { creature: val}
    $.ajax({
        url: 'ajax/add/creature/',
        method: 'POST',
        headers: {
          'Accept': 'application/json',
          'Content-Type': 'application/x-www-form-urlencoded'
        },
        dataType:'json',
        data: keys_set,
      success: function(answer) {
        $('.details').html(answer)
        $('#userinput').val("");
        rebootlinks();
      },
      error: function(answer) {
        $('.details').html('oops, broken')
        rebootlinks();
      },

    });
  });


}

rebootlinks();








