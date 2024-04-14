const inputs = document.querySelectorAll("input");
const submit = document.querySelector("button");

const submit_fn = (event) => {
  event.preventDefault();
  const user = inputs[0].value;
  const pass = inputs[1].value;
  
  fetch('http://127.0.0.1:5000/Users/login', {
    method: 'POST',
    body: JSON.stringify({
      user_name: user,
      password: pass,
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
  })
  .then((response) => response.json())
  .then((json) => {
    console.log(json); // نمایش پاسخ در کنسول
    if (json !== "ok") {
      console.log("خطا رخ داده است");
      document.getElementById("error_text").style.display = "block";
      document.getElementById("login-submit").style.backgroundColor = "red"
    }else {
      document.getElementById("error_text").style.display = "none";
      document.getElementById("login-submit").style.backgroundColor = "green"
      window.open('./t.html')
    }
  })
};



submit.addEventListener("click",submit_fn)
