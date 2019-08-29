/*
           /       '_ /_/ 
          ()(/__/)/(//)/  
            /     _/      
*/
function prepare_ajax(){
  $.ajaxSetup({
    beforeSend: function(xhr, settings) {
      if (!(/^http:.*/.test(settings.url) || /^https:.*/.test(settings.url))) {
        var csrf_middlewaretoken = $('input[name=csrfmiddlewaretoken]').val();        
        xhr.setRequestHeader('X-CSRFToken',csrf_middlewaretoken);
      }
    }
  });
}
 
function loadajax(){
  $.ajax({
    url: 'ajax/list/1/',
    success: function(answer) {            
      $('.charlist').html(answer)
      rebootlinks();
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
        $('.charlist').html(answer)
        rebootlinks();
      },
    });   
  });


  $('#go').off();
  $('#go').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    console.log($('.character_form').serialize());
    console.log($('.character_form input[name=cid]').val());
    var urlupdate = 'ajax/update/character/'+$('.character_form input[name=id]').val();
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
        console.log('Error... '+answer);
      },
    });  
  });

  $('#add_creature').off();
  $('#add_creature').on('click',function(event){
    event.preventDefault();
    $.ajax({
      url: 'ajax/add/creature/',
      success: function(answer) {
        $('.details').html('done')
        rebootlinks();
      },
      error: function(answer) {
        $('.details').html('oops, broken')
        rebootlinks();
      },

    });
  });

  $('#build_config_pdf').off();
  $('#build_config_pdf').on('click',function(event){
    event.preventDefault();
    $.ajax({
      url: 'ajax/build_config_pdf/',
    }).done(function(answer) {
        console.log(answer.comment);
        $('.details').html(answer.comment);
        rebootlinks();
    });
  });

  $('.view_creature').off();
  $('.view_creature').on('click',function(event){
    console.log('View: '+$(this).attr('id'));
    event.preventDefault();
    event.stopPropagation();
    var dad = $(this).parents('li');
    $('li').removeClass('selected');
    $(dad).addClass('selected');
    $.ajax({      
      url: 'ajax/view/creature/'+$(this).attr('id')+'/',
      success: function(answer) {
        $('.details').html(answer)
        $('li').removeClass('selected');
        rebootlinks();
      },
      error: function(answer){
        console.log('Vew error...'+answer);
      }
    });
  });

  $('td.editable.userinput').off();
  $('td.editable.userinput').hover(
    function(event){
      $(this).addClass('focus');
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
    var target = $(this).attr('id')
    var keys = $(this).attr('id').split('_')
    var shift = event.shiftKey
    block = $(this).parent();
    var os = 1;
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
        $('td#'+keys[0]+'_freebiedif').html(answer.freebiedif);
          },
        error: function(answer){
            $('td#'+target).html(answer.new_value);
        },
      });
    });

  $('td.editable.userinput').on('click',function(event){
    event.preventDefault();
    event.stopPropagation();
    var target = $(this).attr('id')
    var keys = $(this).attr('id').split('_')
    var shift = event.shiftKey;
    var val = $('#userinput').val();
    block = $(this).parent();
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
            $('td#'+keys[0]+'_freebiedif').html(answer.freebiedif);
          },
        error: function(answer){
            $('td#'+target).html(answer);
        },
      });
    }
  });
}

rebootlinks();







