function enterHover( posit ){
		var id = '#'+posit
		$(id).css('visibility', 'visible', 'important');
	}

	function leaveHover( posit ){
		var id = '#'+posit
		$(id).css('visibility', 'hidden', 'important');
	}