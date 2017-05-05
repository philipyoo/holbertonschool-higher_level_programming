$.get('http://swapi.co/api/films?format=json', (data) => {
  for (let i = 0; i < data.results.length; i++) {
    $('ul#list_movies').append('<li>' + data.results[i].title + '</li>');
  }
});
