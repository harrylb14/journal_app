oTable = $('#resource_list').DataTable( {
    "sDom": 'lrtip',
    destroy:true,
    "info" : false,
    "pageLength": 5,
    "lengthChange": false,
    "order": [[ 3, "desc" ]],
    "ordering": false,
    "columnDefs": [
     { width: 400, targets: [0,1,2,3] }
    ],
    "fixedColumns": true
})





$('#myInputTextField').keyup(function(){
      $('#resource_list').DataTable().search($(this).val()).draw() ;
});

$('.language').click(function () {
    var language = $(this).text()
    $('.search_filter').html(language);
    $('.search_filter').attr("id", language.trim().toLowerCase() )
});

$('.framework').click(function () {
    var framework = $(this).text()
    $('.search_filter').html(framework);
    $('.search_filter').attr("id", framework.trim().toLowerCase() )
});

$('.search_filter').click(function () {
    $('.search_filter').html('');
    $('.search_filter').attr("id", "hidden" )
})

