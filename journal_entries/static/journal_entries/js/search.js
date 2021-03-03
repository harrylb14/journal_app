$(function () {
    filter = function(){
        var query = $(this).text();
        var classname = $(this).attr('class');
        event.preventDefault()
        $.ajax({

            url: "ajax_search/",
            dataType: 'json',
            data: {
                "class": classname,
                "search": query
            },

            success: function(data){
                $('#resource_list').DataTable().clear()
                $('#resource_list').html(data['html_resource_list'])
                reloadDataform()
            },

        });
    };

    $('.language').click(filter)
    $('.framework').click(filter)
    $('.search_filter').click(filter)

    var reloadDataform = function () {
        $('#resource_list').DataTable( {
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
        $('.language').click(filter)
        $('.framework').click(filter)
        $('.search_filter').click(filter)

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
    }
})
