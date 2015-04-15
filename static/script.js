$(function() {
  $("#like").on('click', function() {
    console.log("Like!");
    var color = $("#current-color").text();
    var song = $("#current-song").text();
    $.ajax({
      type: "POST",
      url: "/like",
      data: { color: color, song: song },
      dataType: 'json',
      success: function(data) {
        console.log(result);
      },
      error: null
    });
  });

  $("#next").on('click', function() {
    console.log("Next!");
    location.reload(true);
  });
});