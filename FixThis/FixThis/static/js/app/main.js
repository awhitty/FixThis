// Initiate the router
var test;
$(document).ready(function () {
   	console.log('document ready');
   	tpl.loadTemplates(['login', 'dashboard'], function() {
   		app = new AppRouter();
   		Backbone.history.start();
   	})
   	

});