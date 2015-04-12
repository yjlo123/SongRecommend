$(function() {
  $("#like").on('click', function() {
    console.log("Liked!");
    $.ajax({
      type: "POST",
      url: "/like",
      data: { color: null },
      dataType: 'json',
      success: function(data) {
        console.log(result);
      },
      error: null
    });
  });
});