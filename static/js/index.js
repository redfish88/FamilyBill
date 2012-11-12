    $(function() {
        $( "#consume_time" ).datepicker({
            showButtonPanel: true,
            dateFormat: 'yy-mm-dd'
        });
        $( "#begin_time" ).datepicker({
            showButtonPanel: true,
            dateFormat: 'yy-mm-dd'
        });
        $( "#end_time" ).datepicker({
            showButtonPanel: true,
            dateFormat: 'yy-mm-dd'
        });
        $( "#accordion" ).accordion({
        	collapsible: true,
        	heightStyle: "content"
        });


      	$.post( "/allMember" , {
    	},
    	function(result) {
    		if(result){
                $('#member_search').append('<option value=0>全部</option>');
                for(var i=0;i<result.length;i++){
                    obj = result[i]
    				option = '<option value='+obj.id+'>'+obj.name+'</option>'
    				$("#member").append(option)
                    $("#member_search").append(option)
    			}
    		}


    	});
        $( "#dialog-form" ).dialog({
            autoOpen: false,
            height: 450,
            width: 500,
            modal: true,
            buttons: {
                "Create a bill": function() {
                     $( "#post_new" ).submit();   
                },
                Cancel: function() {
                    $( this ).dialog( "close" );
                }
            },
            close: function() {
                allFields.val( "" ).removeClass( "ui-state-error" );
            }
        });
        $( "#create-user" )
            .button()
            .click(function() {
                $( "#dialog-form" ).dialog( "open" );
            });

    })
    function fill_accordion( date,name,fee,discription){
        $( '#accordion' ).append('<h3>' + date + ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + name + '</h3>');
        $( '#accordion' ).append('<div><p>金额：' + fee + '</p>'+'<p>' + discription + '</p></div>');

    }
    function ajaxSearch(){
        $.post( "/" , {
            start_time : $( '#start_time' ).val(),
            end_time   : $( '#end_time').val(),
            member_id  : $( '#member_id option:seleted').val()
        },
        function(result) {
            if(result){
                alert(result.length)
                $( '#accordion' ).html('');
                for(var i=0;i<result.length;i++){
                    obj = result[i];

                    fill_accordion(obj.consume_time,obj.name,obj.fee,obj.discription);
                }
                alert(1)
                $( "#accordion" ).accordion({
                    collapsible: true,
                    heightStyle: "content"
                });
                alert(2)

            }

        });
    }


