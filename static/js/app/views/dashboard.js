window.DashboardView = Backbone.View.extend({

    initialize:function () {
        console.log('Initializing Dashboard View');
        this.template = _.template(tpl.get("dashboard"));
    },

    events: {
    },

    render:function () {
        $(this.el).html(this.template());
        $(this.el).attr('id', 'login');
        return this;
    },
});