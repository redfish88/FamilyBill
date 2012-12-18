	function random_one () {
		
	        $.post( "/lottery" , {
	        },
	        function(result) {
	            if(result){
	            	var redballs = result.red;
	            	var blueball = result.blue;
	            	fillBall(redballs,blueball);
	            }


	        });
	}
	function fillBall(redballs,blueball){
		$("#custom").html("");
		for (i in redballs){
			var redball = "<span class='redball'>"+redballs[i]+"</span>";
			$("#custom").append(redball);
		}

		$("#custom").append("<span class='blueball'>"+blueball+"</span>")

	}	

	$(function(){

		random_one();
		$("#try").bind('click',random_one)

	})