$(function(){
  $('#upload').on('click', function() {
    var formdata = new FormData($('#uploadForm').get(0));
    $.ajax({
      type: "POST",
      url: "/upload/",
      data : formdata,
      cache       : false,
      contentType : false,
      processData : false,
      dataType:"json"
    })
    // Ajaxリクエストが成功した場合
    .done(function(data){
      console.log(data['file'])
      $('#result').prop('disabled', false)
      $('#result').children('picture').children('img').attr('src', data['file']);
    })
    // Ajaxリクエストが失敗した場合
    .fail(function(XMLHttpRequest, textStatus, errorThrown){
      alert(errorThrown);
    });
  });

  $('#inference_api').on('click', function() {
    var formdata = new FormData($('#uploadForm').get(0));
    var h = $(window).height();
    $('#overlay').height(h).css('display','block');
    $.ajax({
      type: "POST",
      url: "https://inferenceapi.herokuapp.com/api/inference",
      data : formdata,
      cache       : false,
      contentType : false,
      processData : false,
      dataType:"json"
    })
    // Ajaxリクエストが成功した場合
    .done(function(data){
      console.log(data['file'])
      setTimeout(function(){
        $("#overlay").fadeOut(100);
      },100);
      $('#str_result').text(data['file'])
      $('#str_probality').text(data['probality'])
    })
    // Ajaxリクエストが失敗した場合
    .fail(function(XMLHttpRequest, textStatus, errorThrown) {
      $("#overlay").fadeOut(100);
      alert(errorThrown);
    });
  });
  
  $('#inference').on('click', function() {
    var formdata = new FormData($('#uploadForm').get(0));
    $.ajax({
      type: "POST",
      url: "/inference/",
      data : formdata,
      cache       : false,
      contentType : false,
      processData : false,
      dataType:"json"
    })
    // Ajaxリクエストが成功した場合
    .done(function(data){
      console.log(data['file'])
      $('#str_result').text(data['file'])
      $('#str_probality').text(data['probality'])
    })
    // Ajaxリクエストが失敗した場合
    .fail(function(XMLHttpRequest, textStatus, errorThrown){
      alert(errorThrown);
    });
  });

  $('#inference_for_tensorflow').on('click', function() {
    var formdata = new FormData($('#uploadForm').get(0));
    $.ajax({
      type: "POST",
      url: "/inference/keras",
      data : formdata,
      cache       : false,
      contentType : false,
      processData : false,
      dataType:"json"
    })
    // Ajaxリクエストが成功した場合
    .done(function(data){
      console.log(data['file'])
      $('#str_result').text(data['file'])
      $('#str_probality').text(data['probality'])
    })
    // Ajaxリクエストが失敗した場合
    .fail(function(XMLHttpRequest, textStatus, errorThrown){
      alert(errorThrown);
    });
  });
});