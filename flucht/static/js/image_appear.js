$('.preview-link').click(function(){
	$('.preview').fadeIn();
});

$('.preview').click(function(){
	$(this).fadeOut();
}).children('img').click(function(e) {
	return false;
});
