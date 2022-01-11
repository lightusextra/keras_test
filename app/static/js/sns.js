$(function() {
  createTweet(getUrlParam('comment') + '\n')
  $('#comment').on('change', function() {
    $("#tweet").empty();
    createTweet($('#comment').val())
  });
});
function createTweet(comment) {
  console.log(comment)
  $('<a>').attr({
    id: 'tee',
    href: 'https://twitter.com/share?ref_src=twsrc%5Etfw',
    class: 'twitter-share-button'
  }).appendTo($("#tweet"));
  $('#tee').attr("data-size", "large");
  $('#tee').attr("data-text", comment);
  $('#tee').attr("data-url", "https://murin-an.jp/");
  $('#tee').attr("data-hashtags","無鄰菴");
  $('#tee').attr("data-lang","ja");
  $('#tee').attr("show-count","false");
}
function getUrlParam(name, url) {
  if (!url) url = window.location.href;
  name = name.replace(/[\[\]]/g, "\\$&");
  var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"),
      results = regex.exec(url);
  if (!results) return null;
  if (!results[2]) return '';
  return decodeURIComponent(results[2].replace(/\+/g, " "));
}