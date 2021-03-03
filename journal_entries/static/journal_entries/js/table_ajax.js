$(function () {

  var loadForm = function () {
    var btn = $(this);

    $.ajax({
      url: btn.attr("data-url"),
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-resource").modal("show");
      },
      success: function (data) {
        $("#modal-resource .modal-content").html(data.html_form);
      }
    });
  };


  var saveForm = function () {
    var form = $(this);

    $.ajax({
      url: form.attr("action"),
      data: form.serialize(),
      type: form.attr("method"),
      dataType: 'json',
      success: function (data) {
        if (data.form_is_valid) {
            $("#resource_list tbody").html(data.html_resource_list);
            $("#modal-resource").modal("hide");
            $('#resource_list').DataTable().clear()
            $('#resource_list').html(data['html_resource_list'])
            reloadDataform()
        }
        else {
          $("#modal-resource .modal-content").html(data.html_form);
        }
      }
    });
    return false;
  };


  $(".js-create-resource").click(loadForm);
  $("#modal-resource").on("submit", ".js-resource-create-form", saveForm);

  $("#resource_list").on("click", ".js-update-resource", loadForm);
  $("#modal-resource").on("submit", ".js-resource-update-form", saveForm);

  $("#resource_list").on("click", ".js-delete-resource", loadForm);
  $("#modal-resource").on("submit", ".js-resource-delete-form", saveForm);


  var filter = function(){
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


  var reloadDataform = function () {
    $('#resource_list').DataTable( {
        "sDom": 'lrtip',
        "destroy": true,
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


    $('.language').unbind().click(filter);
    $('.framework').unbind().click(filter);
    $('.search_filter').unbind().click(filter);


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
    });

    $('#myInputTextField').keyup(function(){
        $('#resource_list').DataTable().search($(this).val()).draw() ;
    });
  }

  reloadDataform();
});