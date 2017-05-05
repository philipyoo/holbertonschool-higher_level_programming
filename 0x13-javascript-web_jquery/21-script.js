$.get('https://swapi.co/api/people/5/?format=json', (data) => {
  $('DIV#character').text(data.name);
});
