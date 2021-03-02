oTable = $('#resource_list').DataTable( {
    "sDom": 'lrtip',
    "info" : false,
    "pageLength": 5,
    "lengthChange": false,
    "order": [[ 3, "desc" ]],
    "ordering": false
})



$('#myInputTextField').keyup(function(){
      oTable.search($(this).val()).draw() ;
})
