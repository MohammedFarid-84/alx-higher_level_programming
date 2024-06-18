$(document).ready(function(){
	let url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';
	$.getJSON(url, function(data){
		$('DIV#hello').text(data.hello);
	});
});
