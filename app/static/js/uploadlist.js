$(function(){
  $('#deleteall').on('click', function() {
    var formdata = new FormData($('#uploadForm').get(0));
    $.ajax({
      type: "POST",
      url: "/deletefiles",
      data : formdata,
      cache       : false,
      contentType : false,
      processData : false,
      dataType:"json"
    })
    // Ajaxリクエストが成功した場合
    .done(function(data){
      console.log(data['result'])
      document.location = '/upload/list'
    })
    // Ajaxリクエストが失敗した場合
    .fail(function(XMLHttpRequest, textStatus, errorThrown){
      alert(errorThrown);
    });
  });
});