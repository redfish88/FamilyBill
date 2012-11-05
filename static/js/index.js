    $(function() {
        $( "#create_time" ).datepicker({
            showButtonPanel: true,
            dateFormat: 'yy-mm-dd'
        });
        $( "#accordion" ).accordion({
        	collapsible: true,
        	heightStyle: "content"
        });
      	$.post("/allMember", {
    	},
    	function(result) {
    		if(result){
    			for(var i=0;i<result.length;i++){
    				obj = result[i]
    				option = '<option value='+obj.id+'>'+obj.name+'</option>'
    				$("#member").append(option)
    			}
    		}

    	});

    })
