$(function () {

  $(".js-create-resource").click(function () {
    $.ajax({
      url: '/create/',
      type: 'get',
      dataType: 'json',
      beforeSend: function () {
        $("#modal-resource").modal("show");
      },
      success: function (data) {
        $("#modal-resource .modal-content").html(data.html_form);
      }
    });
  });

  $("#modal-resource").on("submit", ".js-resource-create-form", function () {
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
  });
});