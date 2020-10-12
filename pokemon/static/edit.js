var update = function(description, id){
  var data_to_update = [description, id]
  $.ajax({
      type: "POST",
      url: "/update_description",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_update),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          //var idd = data.toString()
          window.location.href = '/view/'+id
          //$("#"+idd).remove()
          //search(lastSearch)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

$(document).ready(function(){
  $("#submit").click(function(){
    var id = $(location).attr("href").split('/').pop();
    var description = $("#descriptor").val()
    console.log(description)
    update(description, id)
  })
  $("#discard").click(function(){
    var id = $(location).attr("href").split('/').pop();
    window.location.href = '/view/'+id
  })
})
