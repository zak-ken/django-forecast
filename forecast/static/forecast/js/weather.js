google.charts.load('current', {'packages':['table']});

function drawCharts(graph_to_generate) {
    var url = 'ajax/get_graph_data/';
    var param_data = graph_to_generate
    console.log('url == '+url)
    var result = $.ajax({
        url: url,
        dataType: "json",
        data: param_data,
        method: 'post',
        async: false
    }).responseText;
    var json_Data = eval('(' + result + ')');
    console.log('jsonData>> '+json_Data)


    var data = new google.visualization.DataTable();

    data.addColumn('string', 'Date');
    data.addColumn('number', 'min_temp');
    data.addColumn('number', 'max_temp');
    data.addColumn('number', 'wind');
    data.addColumn('string', 'rain');
    data.addRows(json_Data.json_data);

    var table = new google.visualization.Table(document.getElementById('Data_Table_Cont'));

    table.draw(data, {showRowNumber: true, width: '100%', height: '100%' , showRowNumber: true,
    page: 'enable',
    pageSize: 3,
    pagingSymbols: {
        prev: 'prev',
        next: 'next'
    },
    pagingButtonsConfiguration: 'auto'});
}


google.charts.setOnLoadCallback(function(){
        drawCharts({chart_name:'listing_report_table'});
});