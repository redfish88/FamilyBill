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

        $.post( "/allMember" , {
        },
        function(result) {
            if(result){
                $('#member_id').append('<option value=0>全部</option>');
                for(var i=0;i<result.length;i++){
                    obj = result[i]
                    option = '<option value='+obj.id+'>'+obj.name+'</option>'
                    $("#member").append(option);
                    $("#member_id").append(option);
                    $( "#users tbody" ).append( "<tr>" +
                            "<td>" + obj.name + "</td>" + 
                            "<td>" + obj.create_time + "</td>" + 
                            "<td><a href='/del_user/" + obj.id +"' onclick='return confirm(\""+
                            "确定删除该成员？\")'>删除</a></td>" +
                        "</tr>" ); 
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
        $( "#create-bill" )
            .button()
            .click(function() {
                $( "#dialog-form" ).dialog( "open" );
            });
        $( "#user-manage" )
            .button()
            .click(function() {
                $("#target").show('explode',1000);
            });
        $("#target").hide();
        $("#user-hide").button().click(function(){
            $("#target").hide('explode',1000);
        });

    })
    function fill_accordion( id,date,name,fee,discription){
        var entry = '<li><h3>' + date + ' &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;' + name + '</h3>';
        entry = entry + '<p>金额:' + fee + '</p>'+'<p>描述:' + discription + '</p>';
        entry = entry + '<p align="right"><a href=\'/del_bill/'+ id + '\' onclick="return confirm(\'确定删除么？\')"'+
                        '>删除</a></p></li>'
                                        
        $( '#entry' ).append(entry);

    }
    function test_button(){
            $( "#accordion" ).accordion();
    }

    function ajaxSearch(){
        $.post( "/search" , {
            begin_time : $( '#begin_time' ).val(),
            end_time   : $( '#end_time').val(),
            member_id  : $( '#member_id').val()
        },
        function(result) {
            $('#entry').html('');
            if(result.length > 0 ){
                for(var i=0;i<result.length;i++){
                    obj = result[i];

                    fill_accordion(obj.id,obj.consume_time,obj.name,obj.fee,obj.discription);
                }

            }else{
                $('#entry').html('<li>没有相关记录</li>');
            }

        });
    }
    function ajaxCount(){
        $.post( "/count" , {
            begin_time : $( '#begin_time' ).val(),
            end_time   : $( '#end_time').val(),
            member_id  : $( '#member_id').val()
        },
        function(result) {
            $('#entry').html('');
            if(result.length > 0 ){

                for(var i=0;i<result.length;i++){
                    obj = result[i];

                    $('#entry').append('<h3>'+obj.name+'&nbsp;&nbsp;&nbsp;&nbsp;'+obj.count+'</h3>')
                }

            }else{
                $('#entry').html('<li>没有相关记录</li>');
            }

        });
    }


