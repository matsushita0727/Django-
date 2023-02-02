// Cキー押下

function c_click(){
  result.value = "0";
  is_calc = false;
}


// 数字キー押下
function num_click(val){
  
  is_calc = false;


  if(result.value =="0" && val == "0"){
    result.value = "0";
  }else if(result.value == "0" && val == "."){
    result.value = "0.";
  }else if(result.value == "0"){
    result.value = val;
  }else{
    result.value += val;
  }
}

//window.onload = function () {
  


function calc(){
  let element =document.getElementById('total_amount').innerHTML;
  console.log('total_amount');
  //total_amount = input1

  const input2 = document.querySelector("input[name=input2]");
  const change = document.querySelector("input[name=change]");


  change.value = Number(input2.value) - Number(element);
}



