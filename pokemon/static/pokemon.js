var lastSearch = ''
var currentID = ''
var buttonClicked = false
var secondrow=false
var editClicked=false
var abilityClicked=false
var undoClicked=false

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

var update2 = function(description, id){
  var data_to_update = [description, id]
  $.ajax({
      type: "POST",
      url: "/update_pokedex",
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

var getPokedex = function(id){
  var data_to_update = id
  $.ajax({
      type: "POST",
      url: "/get_pokedex",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_update),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          //var idd = data.toString()
          editPokedex(data)
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

var display_search_results = function(pokemon){
  $("#firstcol").empty()
  $("#secondcol").empty()
  console.log(pokemon)

  console.log("Im in here")
  if(pokemon[0].length == 0){
    $("#firstcol").append("No results found")
  }
  else if(window.location.pathname.split("/").pop()=='search'){
    var size = pokemon[0].length
    $("#results").append(size+" results found")

  }

    $.each(pokemon[0], function(i, datum){
      console.log("im working")
      var id = datum["id"].toString()
      var cardID = datum["id"] - 3000
      cardID = cardID.toString()
      var bodyID = datum["id"] + 3000
      bodyID = bodyID.toString()
      var src = datum["picture"]
      var name = datum["name"]
      var new_pokemon = "<div id='"+cardID+"' class='card' style='width: 18rem;''></div>"
      var new_image = "<img id='"+id+"' class='card-img-top pokemon_view pic' src='"+src+"' alt='"+name+"'></div>"
      var new_body = "<div id='"+bodyID+"' class='card-body'></div>"

      var n = name.toLowerCase()
      var s = pokemon[1].toLowerCase()
      console.log(n)
      console.log(s)
      name = n.replace(RegExp(s, 'g'), '<b>' + s + '</b>');
      if(name[0] == '<'){
        name = name[0] + name[1]+ name[2] + name[3].toUpperCase() + name.slice(4)
      }
      else{
        name = name[0].toUpperCase() + name.slice(1)
      }



      if(secondrow){
        $("#secondcol").append(new_pokemon)
        $("#"+cardID).append(new_image)
        $("#"+cardID).append(new_body)
        //$("#"+bodyID).text(name)
        $("#"+bodyID).append(name)

        secondrow = false
      }
      else{
      $("#firstcol").append(new_pokemon)
      $("#"+cardID).append(new_image)
      $("#"+cardID).append(new_body)
      //$("#"+bodyID).text(name)
      $("#"+bodyID).append(name)
      secondrow = true
    }

      //$("#deletes").append(deleteButton)
      //$("#deletes").append("<br>")
    })
    /*
    var iter = 0
    $('.deleteButton').each(function() {
      //test
      var str = pokemon[iter]["id"]
      var str = str.toString();
      $(this).val(str);
      iter = iter+1;
    });
    $("#searchbox").val('')
    $("#searchbox").focus();
    */
}



var editDescription = function(){
  $("#edit").remove()
  var description = $("#description").text()
  var editField = "<input id=editField type=textarea></input>"
  var submit = '<button id="sub" class="submit">Submit';
  var discard = '<button class="discard">Discard Changes';

  $("#description").replaceWith(editField)
  //$("#description").append(submit)
  $("#editField").after(submit)
  //$("#edit").replaceWith(submit)
  $("#sub").after(discard)
  $("#editField").val(description)
  $("#editField").focus()

}

var editPokedex = function(pokedex){
  $("#edit2").remove()

  var editField = "<input id=editField2 type=textarea></input>"
  var submit = '<button id="sub2" class="submit2">Submit';
  var discard = '<button class="discard">Discard Changes';

  $("#pokedex").replaceWith(editField)
  //$("#description").append(submit)
  $("#editField2").after(submit)
  //$("#edit").replaceWith(submit)
  $("#sub2").after(discard)
  $("#editField2").val(pokedex)
  $("#editField2").focus()

}
var display_ten = function(pokemon){
  $("#firstcol").empty()
  $("#secondcol").empty()
  console.log(pokemon)

  console.log("Im in here")
  if(pokemon.length == 0){
    $("#firstcol").append("No results found")
  }
  else if(window.location.pathname.split("/").pop()=='search'){
    var size = pokemon.length
    $("#results").append(size+" results found")

  }

    $.each(pokemon, function(i, datum){
      console.log("im working")
      var id = datum["id"].toString()
      var cardID = datum["id"] - 3000
      cardID = cardID.toString()
      var bodyID = datum["id"] + 3000
      bodyID = bodyID.toString()
      var src = datum["picture"]
      var name = datum["name"]
      var new_pokemon = "<div id='"+cardID+"' class='card' style='width: 18rem;''></div>"
      var new_image = "<img id='"+id+"' class='card-img-top pokemon_view pic' src='"+src+"' alt='"+name+"'></div>"
      var new_body = "<div id='"+bodyID+"' class='card-body'></div>"

      if(secondrow){
        $("#secondcol").append(new_pokemon)
        $("#"+cardID).append(new_image)
        $("#"+cardID).append(new_body)
        $("#"+bodyID).text(name)
        secondrow = false
      }
      else{
      $("#firstcol").append(new_pokemon)
      $("#"+cardID).append(new_image)
      $("#"+cardID).append(new_body)
      $("#"+bodyID).text(name)

      secondrow = true
    }

      //$("#deletes").append(deleteButton)
      //$("#deletes").append("<br>")
    })
    /*
    var iter = 0
    $('.deleteButton').each(function() {
      //test
      var str = pokemon[iter]["id"]
      var str = str.toString();
      $(this).val(str);
      iter = iter+1;
    });
    $("#searchbox").val('')
    $("#searchbox").focus();
    */
}


var ten = function(query){
  var data_to_search = query
  $.ajax({
      type: "POST",
      url: "ten_names",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_search),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          display_ten(data)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

var search = function(query){
  var data_to_search = query
  $.ajax({
      type: "POST",
      url: "search_name",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_search),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          display_search_results(data)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

var save = function(query){
  var data_to_search = query
  $.ajax({
      type: "POST",
      url: "/save_name",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_search),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          window.location.href = '/search'
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

var delete_name = function(id){
  var data_to_delete = id
  $.ajax({
      type: "POST",
      url: "delete_name",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_delete),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          var idd = id.toString()
          //$("#"+idd).remove()
          search(lastSearch)
      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

var mark_deleted = function(id, ability){
  var data_to_delete = [id, ability]
  $.ajax({
      type: "POST",
      url: "/delete_attr",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_delete),

      success: function(result){

          var all_data = result["data"]
          data = all_data


      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

var undo = function(id, ability){
  var data_to_undo = [id, ability]
  $.ajax({
      type: "POST",
      url: "/undo",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_undo),

      success: function(result){

          var all_data = result["data"]
          data = all_data


      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}

/*
var view = function(id){
  var data_to_view = id
  $.ajax({
      type: "POST",
      url: '/view/<id>',
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_view),

      success: function(result){

          var all_data = result["data"]
          data = all_data

      },
      error: function(request, status, error){
          console.log("Error");
          console.log(request)
          console.log(status)
          console.log(error)
      }
  });
}
*/

$(document).ready(function(){

  if(window.location.pathname.split("/").pop()!='search'){
    ten("test")

  }
  else if(window.location.pathname.split("/").pop()=='search'){
    search("test")
  }


  $("#search").click(function(){
    console.log("clicked")
    var query = $("#searchbox").val()
    lastSearch = query
    console.log(query)
    //window.location.href = '/search'
    save(query)

  })
  $("#searchbox").keyup(function(event) {
    if (event.keyCode === 13) {
        $("#search").click();
    }
  });

  $(document).on('click', '.pokemon_view', function(){
    if(!buttonClicked){
    console.log("this pokemon was clicked")
    var id = $(this).attr('id')
    currentID = id
    //view(id)
    window.location.href = '/view/'+id
  }
  else{
    buttonClicked = false
  }

  });
  $(document).on('click', '.deleteButton', function(){
    buttonClicked = true
    var val = $(this).val();
    val = parseInt(val);
    console.log(val)
    delete_name(val)
    //$(this).remove()


  })

  $(document).on('click', '.ability', function(){

    if(!abilityClicked){
      var id = $(location).attr("href").split('/').pop();
      var ability = $(this).attr('id')
      console.log(ability)
      var together = "#"+ability
      console.log(together)
      var parent = $(this).parent()

      var undo = "<button id='"+ability+"' class=undo>Undo"
      $(parent).replaceWith(undo)
      mark_deleted(id, ability)
      abilityClicked = true
    }
    else{
      abilityClicked = false
    }


  });

  $(document).on('click', '.undo', function(){

    if(!undoClicked){
      var id = $(location).attr("href").split('/').pop();
      var ability = $(this).attr('id')
      console.log(ability)
      var outer = "<div id=temp>"+ability+""
      var button = " <button id='"+ability+"' class=ability>X"
      $(this).replaceWith(outer)
      $("#temp").append(button)
      $("#temp").removeAttr('id')

      undo(id, ability)
      undoClicked = true
    }
    else{
      undoClicked = false
    }


  });

  $("#edit").click(function(){
    console.log("edit")
    if(!editClicked){
      editDescription()
      editClicked = true
    }
    else{
      editClicked = false
    }

    //var id = $(location).attr("href").split('/').pop();
    //window.location.href = '/edit/'+id
  })

  $("#edit2").click(function(){
    console.log("edit2")
    if(!editClicked){
      var id = $(location).attr("href").split('/').pop();
      getPokedex(id)
      //editPokedex()
      editClicked = true
    }
    else{
      editClicked = false
    }

    //var id = $(location).attr("href").split('/').pop();
    //window.location.href = '/edit/'+id
  })
  $(document).on('click', '#sub2', function(){
    var id = $(location).attr("href").split('/').pop();
    var pokedex = $("#editField2").val()
    console.log(pokedex)
    update2(pokedex, id)
  })

  $(document).on('click', '.submit', function(){
    var id = $(location).attr("href").split('/').pop();
    var description = $("#editField").val()
    console.log(description)
    update(description, id)
  })
/*
  $("#discard").click(function(){
    console.log("discard")
    location.reload()
  })
*/
  $(document).on('click', '.discard', function(){
    console.log("discard")
    location.reload()


  })
})
