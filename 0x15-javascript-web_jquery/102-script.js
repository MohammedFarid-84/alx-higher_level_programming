$(document).ready(function(){
    $('#btn_translate').click(function(){
        let url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val();
        $.getJSON(url, function(data){
            //alert($('#language_code').val());
            $('#hello').text(data.hello);
        }); 
    });
    $('#language_code').keypress(function(e){
        if (e.which == 13){
            let url = 'https://hellosalut.stefanbohacek.dev/?lang=' + $('#language_code').val();
            $.getJSON(url, function(data){
                $('#hello').text(data.hello);
            }); 
        }
    });
});
