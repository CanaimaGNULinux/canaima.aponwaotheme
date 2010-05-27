jQuery(function() {
	
	jQuery("#menu ul").lavaLamp({
		fx: "easeOutBack",
		speed: 700
    });
    
    jQuery("#controller").jFlow({
		slides: ".slides",
		width: "960px",
		height: "210px",
controller: ".jFlowControl", // must be class, use . sign
auto: true,     //auto change slide, default true
duration: 700,
prev: ".jFlowPrev", // must be class, use . sign
next: ".jFlowNext" // must be class, use . sign
	});
    
    jQuery('#twitter_msg').twitterize('CanaimaLinux');
    
});
