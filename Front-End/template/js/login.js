document.getElementById('submit').addEventListener('click', function(event) {
    event.preventDefault();

    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    fetch('http://127.0.0.1:5000/Users/login', {
        method: 'POST',
        body: JSON.stringify({
            username: username,
            password: password
        }),
        headers: {
            'Content-type': 'application/json; charset=UTF-8'
        }
    })
    .then(response => response.json())
    .then(response => {
        if (response === "ok") {
            window.alert('ورود به سیستم با موفقیت انجام شد');
            window.location.href = 'index.html';
        } else {
            window.alert('نام کاربری یا رمز عبور اشتباه است');
        }
    });
});
































// var username
// var password

// document.getElementById('submit').addEventListener('click', function(event) {
//     event.preventDefault(); 
//     username = document.getElementById('username').value;
//     password = document.getElementById('password').value;

//     fetch('http://127.0.0.1:5000/Users/login', {
//         method: 'POST',
//         body: JSON.stringify({
//             username: username,
//             password: password,
//         }),
//         headers: {
//             'Content-type': 'application/json; charset=UTF-8',
//         },
//     })
//     .then((response) => response.json())
//     .then((json) => {
//         if (json !== "ok") {
//             window.alert("نام کاربری یا رمز عبور اشتباه است");
//         }else {
//             window.alert("با موفقیت وارد شدین");
//             window.open('index.html')
//         }
//     })
// });