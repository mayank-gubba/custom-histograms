var data
$('#run_normal').click(function(){
    $.ajax({
        url: "/bar1",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'rep': document.getElementById('replaces').value,
            'mean':document.getElementById('mean').value,
            'sd':document.getElementById('sd').value,
            'samp':document.getElementById('samp').value,
        },
        layout : {
            title:'Scatter plot of shared tokens',
            hovermode:'closest',
         },
        dataType:"json",
        success: function (data, layout) {
            var myplot = document.getElementById('bargraph')
            Plotly.newPlot('bargraph', data)
            myplot.on('plotly_hover', function(data){
                colors = 'orange';
                var update = {'marker':{color: colors}};
                Plotly.restyle('bargraph', update);
              }),
            myplot.on('plotly_unhover', function(data){
                colors = '#00000';
              
                var update = {'marker':{color: colors}};
                Plotly.restyle('bargraph', update);
              });
        },
        On_error : function(){
            console.log('error ')
        }

     });
})
$('#run_uniform').click(function(){
    console.log('lord gubba')
    $.ajax({
        url: "/bar2",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'rep': document.getElementById('replaces').value,
            'min':document.getElementById('min').value,
            'max':document.getElementById('max').value,
            'samp':document.getElementById('samp').value
        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph', data );
        }
    });

})
$('#run_exponential').click(function(){
    console.log('lord gubba')
    $.ajax({
        url: "/bar3",
        type: "GET",
        contentType: 'application/json;charset=UTF-8',
        data: {
            'rep': document.getElementById('replaces').value,
            'lambda':document.getElementById('lambda').value,
            'samp':document.getElementById('samp').value
            
        },
        dataType:"json",
        success: function (data) {
            Plotly.newPlot('bargraph', data );
        }
    });

})
