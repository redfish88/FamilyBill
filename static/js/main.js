
$(document).ready(function() {

        $.post("/report",
            function(result){
                var json = eval(result);
                chart1 = new Highcharts.Chart({
                     chart: {
                        renderTo: 'container',
                        type: 'spline',
                        height: 350,
                     },
                     title: {
                        text: '消费记录'
                     },
                     xAxis: {
                        categories: json.categories
                     },
                     yAxis: {
                        title: {
                           text: 'Interviewed'
                        }
                     },
                     series: json.series
                    });
            });



})