$(document).ready(function(){
	$('DIV#toggle_header').click(function(){
		if ($(this).hasClass('green')) {
			$(this).removeClass('green').addClass('red');
		} else {
			$(this).removeClass('red').addClass('green');
		}
	});
});
