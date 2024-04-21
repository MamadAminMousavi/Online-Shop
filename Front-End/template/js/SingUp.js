document.getElementById('submit').addEventListener('click', function(event) {
    event.preventDefault();

    var inputUsername = document.getElementById('username').value;
    var inputPassword = document.getElementById('password').value;
    var inputEmail = document.getElementById('email').value;
    var inputPhonenumber = document.getElementById('phonenumber').value;
    var inputShippingaddress = document.getElementById('shippingaddress').value;

    fetch('http://127.0.0.1:5000/Users', {
        method: 'POST',
        body: JSON.stringify({
            Name: inputUsername,
            Password: inputPassword,
            Email: inputEmail,
            Phone: inputPhonenumber,
            Role: "User",
            address: inputShippingaddress,
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8',
        },
    })
    .then(response => response.json())
    .then(response => {
        if (response !== "NO") {
            window.alert('ثبت نام با موفقیت انجام شد');
            window.open('index.html');
        } else {
            window.alert('ثبت نام انجام نشد');
        }
    });
});
