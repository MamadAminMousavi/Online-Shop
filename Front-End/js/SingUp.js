const inputs = document.querySelectorAll("input");
const submit = document.querySelector("button");

const submit_fn = (event) => {
  event.preventDefault();
  const user = inputs[0].value;
  const pass = inputs[2].value;
  const email = inputs[1].value;
  const phone = inputs[3].value;
  const address = inputs[4].value;
  console.log(inputs)
  event.preventDefault();
  fetch('http://127.0.0.1:5000/Users', {
    method: 'POST',
    body: JSON.stringify({
      Name: user,
      Password: pass,
      Email: email,
      Phone: phone,
      address: address,
      Role: "User",
    }),
    headers: {
      'Content-type': 'application/json; charset=UTF-8',
    },
  })
  .then((response) => response.json())
  .then((json) => {
    console.log(json); // نمایش پاسخ در کنسول
    if(json != "NO"){
      window.open('./login.html');
    }else {
      window.alert("error");
    }
  })
};


submit.addEventListener("click",submit_fn)

