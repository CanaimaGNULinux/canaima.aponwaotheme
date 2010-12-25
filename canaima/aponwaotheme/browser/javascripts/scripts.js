jQuery(

	function() {

		jQuery("#menu ul").lavaLamp({
			fx: "easeOutBack",
			speed: 700
   		 });
    
		jQuery("#controller").jFlow({
			slides: ".slides",
			width: "960px",
			height: "300px",
			controller: ".jFlowControl",
			auto: true,
			duration: 700,
			prev: ".jFlowPrev",
			next: ".jFlowNext"
		});
  
});
