var nameError=false;
var pictureError=false;
var descriptionError=false;
var pokedexError=false;
var ability1Error=false;


var startover = function(id){

  var button = "<button id='"+id+"' class='seeNow'>See it here</button>"
  $("#name").val("");
  $("#picture").val("");
  $("#description").val("")
  $("#pokedex").val("");
  $("#ability1").val("");
  $("#ability2").val("");
  $("#ability3").val("");
  $("#ability4").val("");
  $("#newitem").text("New item succesfully created.")
  $("#newitem").append(button)
  $("#name").focus();

}
var checkFields = function(){

  newName = $("#name").val();
  newPicture = $("#picture").val();
  newDescription = $("#description").val()
  newPokedex = $("#pokedex").val();
  newAbility1 = $("#ability1").val();
  newAbility2 = $("#ability2").val();
  newAbility3 = $("#ability3").val();
  newability4 = $("#ability4").val();

  $("#nError").remove();
  $("#pError").remove();
  $("#dError").remove();
  $("#pdexError").remove();
  $("#aError").remove();

  if ( $.trim(newName) == '' || $.trim(newPicture) == '' || $.trim(newDescription) == '' || $.trim(newPokedex) == '' || isNaN($.trim(newPokedex)) || $.trim(newAbility1) == ''){
    $("#nError").remove();
    $("#pError").remove();
    $("#dError").remove();
    $("#pdexError").remove();
    $("#aError").remove();



    if($.trim(newDescription) == ''){
    if(!descriptionError){
    $("#description").after('<span id="dError">You must provide a description</span>');
    descriptionError = true;
    }
    else{
      $("#dError").remove();
      $("#description").after('<span id="dError">You must provide a description</span>');
    }

    $("#description").focus();
    }
    if($.trim(newAbility1) == ''){
    if(!ability1Error){
    $("#ability1").after('<span id="aError">You must provide an ability</span>');
    ability1Error = true;
    }
    else{
      $("#aError").remove();
      $("#ability1").after('<span id="aError">You must provide an ability</span>');
    }
    $("#ability1").focus();
    }
    if($.trim(newPokedex) == ''){
    if(!pokedexError){
    $("#pokedex").after('<span id="pdexError">You must provide a pokedex</span>');
    pokedexError = true;
    }
    else{
      $("#pdexError").remove();
      $("#pokedex").after('<span id="pdexError">You must provide a pokedex</span>');
    }

    $("#pokedex").focus();
    }
    else if(isNaN($.trim(newPokedex))){
      if(!pokedexError){
      $("#pokedex").after('<span id="pdexError">You must provide a number</span>');
      pokedexError = true;
      }
      else{
        $("#pdexError").remove();
        $("#pokedex").after('<span id="pdexError">You must provide a number</span>');
      }
      $("#pokedex").focus();
    }
    if($.trim(newPicture) == ''){
    if(!pictureError){
    $("#picture").after('<span id="pError">You must provide a url</span>');
    pictureError = true;
    }
    else{
      $("#pError").remove();
      $("#picture").after('<span id="pError">You must provide a url</span>');
    }

    $("#picture").focus();
    }
    if($.trim(newName) == ''){
    if(!nameError){
    $("#name").after('<span id="nError">You must provide a name</span>');
    nameError = true;
    }
    else{
      $("#nError").remove();
      $("#name").after('<span id="nError">You must provide a name</span>');
    }

    $("#name").focus();
    }
  }

  else{
    createPokemonData()
  }
}

var createPokemonData = function(){

  newName = $("#name").val();
  newPicture = $("#picture").val();
  newDescription = $("#description").val()
  newPokedex = $("#pokedex").val();
  newAbility1 = {"name":$("#ability1").val(), "delete":false}
  newAbility2 = {"name":$("#ability2").val(), "delete":false}
  newAbility3 = {"name":$("#ability3").val(), "delete":false}
  newAbility4 = {"name":$("#ability4").val(), "delete":false}

  if(newAbility2["name"]==""){
    newAbility2["delete"]=true
  }
  if(newAbility3["name"]==""){
    newAbility3["delete"]=true
  }
  if(newAbility4["name"]==""){
    newAbility4["delete"]=true
  }

  data = {
    "name":newName,
    "picture":newPicture,
    "description":newDescription,
    "Pokedex":newPokedex,
    "Abilities":[newAbility1, newAbility2, newAbility3, newAbility4]
  }
  createPokemon(data)

}

var createPokemon = function(pokemon){
  var data_to_create = pokemon
  $.ajax({
      type: "POST",
      url: "create_name",
      dataType : "json",
      contentType: "application/json; charset=utf-8",
      data : JSON.stringify(data_to_create),

      success: function(result){

          var all_data = result["data"]
          data = all_data
          var id = data["id"]
          startover(id)
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
    checkFields()
  })
  $(document).on('click', '.seeNow', function(){
    var id = $(this).attr('id')
    window.location.href = '/view/'+id

  });



})
