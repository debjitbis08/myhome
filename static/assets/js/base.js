$(function() {

  //Load Markdown help section
  if ($('#commentForm').length > 0){
    $('#markdownhelp').find('.contentWrap').load('/media/assets/static/markdownhelp.html #dingus');
    $('#commentForm').find('a[rel="#markdownhelp"]').click(function () {
      $('#markdownhelp').show();
      return false;
    });
    $('#markdownhelp').find('div.close img').click(function () {
      $('#markdownhelp').hide();
    });
  }
});

