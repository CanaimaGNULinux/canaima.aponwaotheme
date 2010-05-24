(function($){

$.fn.twitterize = function(username,options){
   
    if (username){

        var defaultSettings = {
            count:'1'
        }
        var settings = $.extend(defaultSettings, options);

        var url = "http://twitter.com/status/user_timeline/"+username+".json?count="+settings.count+"&callback=?";

        var holder = this;
       
        $.getJSON(url,
        function(data){

            $.each(data, function(i, item) {

                holder.replaceWith(item.text.makeLinks());
   
            });
        });
       
    }else{

        console.debug("jquery plugin twitterize requires a username! Check your parameters");

    }
   
    String.prototype.makeLinks = function() {
        return this.replace(/[A-Za-z]+:\/\/[A-Za-z0-9-_]+\.[A-Za-z0-9-_:%&\?\/.=]+/, function(str) {
        return str.link(str);
        });
    };

   
return this;

};

})(jQuery);
