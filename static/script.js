$("#like").on('click', function() {
  $.ajax({
    type: "POST",
    url: "/like",
    data: {  },
    dataType: 'json',
    success: callback
  });
});