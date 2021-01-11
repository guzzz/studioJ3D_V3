
var $grid = $('.grid').masonry({
	itemSelector: '.grid-item',
	percentPosition: true,
	columnWidth: '.grid-sizer',
	gutter: 1
});

$grid.imagesLoaded().progress( function() {
	$grid.masonry();
});  
