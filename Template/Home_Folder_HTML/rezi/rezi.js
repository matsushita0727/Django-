function get_calc(btn3) {
    if(btn3.value == "=") {
      document.dentaku.display.value = eval(document.dentaku.display.value);
    } else if (btn3.value == "C") {
      document.dentaku.display.value = "";
    } else {
      if (btn3.value == "*") {
        btn3.value = "*";
      } else if (btn3.value == "÷") {
        btn3.value = "/";
      }
      document.dentaku.display.value += btn3.value;
      document.dentaku.add_btn.value = "*";
      document.dentaku.div_btn.value = "÷";
    }
  }

