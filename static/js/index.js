    $(function() {
        $( "#create_time" ).datepicker({
            showButtonPanel: true,
            dateFormat: 'yy-mm-dd'
        });
        $( "#create_time" ).datepicker($.datepick.regional['zh-CN']);
    });
