async function play() {
  eel.intro()
}


async function number() {
  
  let place = document.getElementById('input_number').value

  let result1= await eel.value(place)()
  let result2= await eel.guest()()
  
  document.getElementById("abc").innerHTML = result1;
  setTimeout(function(){ 
      document.getElementById("abc").innerHTML = "";
  document.getElementById("input_number").value="";
}, 1500);
document.getElementById("abcd").innerHTML = result2;
}

