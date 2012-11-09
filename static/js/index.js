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
