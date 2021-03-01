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

//  $('.pagination a').click(function(event){
//    event.preventDefault();
//    var page_no = $(this).attr('href');
//    // ajax
//        $.ajax({
//                type: "POST",
//                url: "{% url 'journal_entries:ajax_pagination' %}",
//                data : {
//                    page_no : page_no,
//                csrfmiddlewaretoken: '{{ csrf_token }}',
//            },
//            success: function (resp) {
//                //loop
//                $('#resource_list tbody').html('')
//               $.each(resp.results, function(i, val) {
//                 //apending posts
//                $('#resource_list tbody').append('<h2>' + val.title + '</h2>')
//               });
//            },
//            error: function () {}
//        }); //

//});

});