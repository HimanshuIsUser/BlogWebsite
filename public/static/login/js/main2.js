
function register(){
    let email = document.getElementById('email').value;
    let name= document.getElementById('username').value;
    let password = document.getElementById('password').value;
    var csrf = document.getElementById('csrf').value;

    if (email == ''){
        alert('Email is required')
    }
    else if(password==''){
        alert('Password is required')
    }
    var data = {
        'email' : email,
        'password':password,
        'name':name
    }
    fetch('/login/register/',{
        method : 'POST',
        headers: {
            'Content-Type':'application/json',
            'X-CSRFToken':csrf,
        },
        body : JSON.stringify(data)
    }).then(result => result.json())
    .then(response => { 
        console.log('response:', response.data.email);
        if (response.status === 200){
            localStorage.setItem('access_token',response.accessToken)
            localStorage.setItem('id',response.user)
            window.location.href = '/blog/';
        }
        else{
            console.log(response);
            alert(response.message);
        }
    })
    .catch(error => {
        console.error(error);
        alert('An error occurred during registration. Please try again later.');
    });
}