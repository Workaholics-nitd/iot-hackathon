createHumidity();

function getData(min = 0, max = 1) {
    return (Math.random()*(max-min)+min);
}

var pre_layout = {
    paper_bgcolor: 'white',
    font: {
        family :  'Roboto',
        size   :  12,
        color  :  '#444'
    },
    width: 600,
    height: 400,
    xaxis: {
        type: "date",
        tickformat: "%X", //to display time formatted as hh:mm:ss
        showline: false,
        autotick: true,
        gridcolor: 'rgb(238, 238, 238)',
        gridwidth: 1,
        showgrid:  true,
        zerolinecolor: '#444',
        zerolinewidth: 1,
        zeroline:  true,
        anchor:    'y1',
        
    },
    yaxis: {
        rangemode: "nonnegative",
        titlefont: {
            family :  'Roboto',
            size   :  12,
            color  :  '#444'
        },
        anchor:    'x1',
        range: [15, 45],
    },
};

function createTemp(){
    var tempDiv = document.getElementById('temperature');

    var traceA = {
        x: [1, 2, 3, 4, 5, 6, 7],
        y: [35, 40.5, 29.8, 40, 41, 39, 35],
        type: 'scatter'
    };

    var data = [traceA];
    var layout = pre_layout;
    
    Plotly.plot( tempDiv, data, layout );
}

function createHumidity(){
    var tempDiv = document.getElementById('humidity');

    var traceA = {
        x: [1, 2, 3, 4, 5, 6, 7],
        y: [35, 40.5, 29.8, 31.2, 29, 35, 40],
        type: 'scatter'
    };

    var data = [traceA];
 
    var layout = pre_layout;
    
    Plotly.plot( tempDiv, data );
    
    var cnt = 8;
    var interval = setInterval(function(){

        Plotly.extendTraces(tempDiv,{
            x: [[cnt]],
            y: [[getData(15, 45)]]
        },[0],10);

        cnt ++;
        if(cnt === 100) clearInterval(interval);
    },2000);
}