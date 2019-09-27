// movies title by using this URL: https://swapi.co/api/films/?format=json

$.get('https://swapi.co/api/films/?format=json', function (data) {
    const film = data.results;
    for (const i of film) {
	$('UL#list_movies').append('<li>' + i.title + '</li>');
    }
});
