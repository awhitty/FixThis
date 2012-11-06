// this code is from http://coenraets.org/blog/2012/03/using-backbone-js-with-jquery-mobile/

// to use Backbone's routing, we have to disable jQM's routing
$(window).bind("load", function () {
    // $.mobile.ajaxEnabled = false;
    // $.mobile.linkBindingEnabled = false;
    // $.mobile.hashListeningEnabled = false;
    // $.mobile.pushStateEnabled = false;
});

// we also have to remove hidden pages from the DOM when they aren't used
$('div[data-role="page"]').on('pagehide', function (event, ui) {
    $(event.currentTarget).remove();
});

var AppRouter = Backbone.Router.extend({
 
    routes:{
        "":           "dashboard",
        "dashboard":  "dashboard",
        "login":      "login",
        "map":        "mapRequests",
        "list":       "listRequests",
        "detail/:id": "requestDetail",

    },

    initialize:function () {
        // Handle back button throughout the application
        $('.back').on('click', function(event) {
            window.history.back();
            return false;
        });

        this.firstPage = true;
        // this.changePage(new DashboardView());
    },


 
    dashboard:function () {
        this.changePage(new DashboardView());
    },

    // map:function() {
    //     this.changePage(new MapView());
    // },
 
    login:function () {
        this.changePage(new LoginView())
    },
 
    changePage:function (page) {
        // $(page.el).attr('data-role', 'page');
        page.render();
        $('body').append($(page.el));
        $.mobile.changePage($(page.el), {changeHash:false});
    }, 
});








