$.getJSON('https://swapi-api.hbtn.io/api/films/?format=json', data => {

  // data['results'] is an array | (index, movie) allows $.each
  // to break up an array like a dictionary into indexes and values
  $.each(data['results'], (index, movie) => {
    $('#list_movies').append('<li>' + movie['title'] + '</li>');
  });

});
