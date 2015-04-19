$(function() {
  $("#like").on('click', function() {
    console.log("Like!");
    $("#like").text("Sending...");
    var color = $("#current-color").text();
    var song = $("#current-song").attr("href");
    $.ajax({
      type: "POST",
      url: "/like",
      data: { color: color, song: song },
      dataType: 'json',
      success: $("#like").text("Liked!"),
      error: null
    });
  });

  $("#next").on('click', function() {
    console.log("Next!");
    location.reload(true);
  });
});