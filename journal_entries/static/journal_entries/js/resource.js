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

});