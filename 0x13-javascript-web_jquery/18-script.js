$('div#toggle_header').on('click', function () {
  $('header').toggleClass(function () {
    return $(this).hasClass('red') ? 'green' : 'red';
  });
});
