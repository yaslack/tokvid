function changeColor(){
    document.body.style.backgroundColor = "blue";
}
input=document.querySelector('[name="url"]')
input.style.width = input.value.length = input.getAttribute('placeholder').length-12+"ch";

var x = document.getElementById("loadingSubmit");
x.style.display = "none";

function validate() {

    var y = document.getElementById("buttonSubmit");
    y.style.display = "none";
    var x = document.getElementById("loadingSubmit");
    x.style.display = "block";
      
}

function submitForm(){
    validate()
    document.getElementById("theForm").submit();
}