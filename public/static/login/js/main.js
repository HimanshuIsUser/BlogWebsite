


function login(){
    var username = document.getElementById('loginusername').value;
    var password = document.getElementById('loginpassword').value;
    var csrf = document.getElementById('csrf').value;

    if (username=='' && password==''){
        alert('You have to enter both')
    }

    var data = {
        'email':username,
        'password':password
    }

    fetch('/login/login/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => { 
        console.log('response:', response);
        if (response.status === 200){
            console.log(response.access_token);
            localStorage.setItem('access_token',response.access_token)
            localStorage.setItem('id',response.user)
            console.log(localStorage.getItem('access_token'))
            window.location.href = '/blog/';
        }
        else{
            console.log('No user Found');
            alert('No User Found');
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during login. Please try again later.');
    });

}

console.log('done')
const accessToken = localStorage.getItem('access_token');
const loginButton = document.getElementById('login-button');
const logoutButton = document.getElementById('logout-button');

  if (accessToken) {
    console.log(accessToken)
    // If an access token is present, show the logout button and hide the login button
    logoutButton.style.display = 'inline-block';
    loginButton.style.display = 'none';
  } else {
    // If no access token is present, show the login button and hide the logout button
    loginButton.style.display = 'inline-block';
    logoutButton.style.display = 'none';
  }

function logout() {
    // Remove the access token from localStorage and hide the logout button
    localStorage.removeItem('access_token');
    logoutButton.style.display = 'none';
    loginButton.style.display = 'inline-block';
}


function addblog(){
    let accessToken = localStorage.getItem('access_token')
    if (accessToken){
        fetch('/api/protected/?access_token=' + accessToken, {
            method: 'GET',
            headers: {
            'Content-Type': 'application/json'
            }
        })
    }
    else{
        alert('Login Requied')
    }
}
