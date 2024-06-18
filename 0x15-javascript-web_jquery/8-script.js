$(document).ready(function(){
	let url = 'https://swapi-api.alx-tools.com/api/films/?format=json';
	$.getJSON(url, function(data){
		$.each(data.results, function(index, movi){
		$('UL#list_movies').append('<li>' + movi.title + '</li>');
		});
	});
});
