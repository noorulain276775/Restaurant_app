const registerForm = document.getElementById('signup_form')
const signinForm = document.getElementById('signin_form')

$('#login').click(function () {
    $.ajax({
        url: 'login',
        method: "GET",
        success: function () {
            $('#id01').show();
            console.log("Get login endpoint")
        },
        error: function () {
            console.log("Something went wrong at login get endpoint")
        }
    })
});

$('#auth').click(function () {
    $.ajax({
        url: 'register',
        method: "GET",
        success: function () {
            $("#login").removeClass("login-select");
            $("#signup").addClass("login-select");
            $("#loginbox").hide(300);
            $("#signupbox").show(300);
            console.log("Get register endpoint")
        },
        error: function () {
            console.log("Something went wrong at register get endpoint")
        }
    })
});

$('#signup').click(function () {
    $.ajax({
        url: 'register',
        method: "GET",
        success: function () {
            console.log("Get register here")
        },
        error: function () {
            console.log("Something went wrong at register get endpoint")
        }
    })
});

registerForm.addEventListener('submit', function (e) {
    e.preventDefault()
    const email = $('#id_email').val()
    const password = $('#id_password').val()
    const password2 = $('#id_password2').val()
    $.ajax({
        headers: {
            "X-CSRFToken": csrftoken
        },
        url: 'register',
        method: 'POST',
        data: {
            email: email,
            password: password,
            password2: password2,
        },
        success: function (data) {
            if (data) {
                $("#signup").removeClass("login-select");
                $("#login").addClass("login-select");
                $("#signupbox").hide(300);
                $("#loginbox").show(300);
                console.log("User has been successfully created")
                alert('Account has been created')
            }
        },
        error: function () {
            console.log("Something happened");
            alert('SOmething went wrong at register post method')

        }
    })
});


signinForm.addEventListener('submit', function (e) {
    e.preventDefault()
    const email = $('#email_id').val()
    const password = $('#password_id').val()
    $.ajax({
        headers: {
            "X-CSRFToken": csrftoken
        },
        url: 'login',
        method: 'POST',
        data: {
            email: email,
            password: password,
        },
        success: function (data) {
            if (data) {
                console.log("you are logged in!")
                handleAlerts("success", "You are logged-in successfully")
                $.ajax({
                    headers: {
                        "X-CSRFToken": csrftoken
                    },
                    url: 'menu',
                    method: 'GET',
                    success: function () {
                        window.location.href = 'menu';
                        console.log("Items has been successfully retrieved /menu")
                    },
                    error: function () {
                        console.log("An error occured at /menu")
                    }
                })
            }
        },
        error: function () {
            console.log("Something happened");
            alert('SOmething went wrong')

        }
    })
});

const getCookie = (name) => {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken)


function openmenu(){
    $.ajax({
        url: 'menu',
        method: 'GET',
        success: function(){
            window.location.href = 'menu';
            console.log("Menu Opened /menu from landing page")
        },
        error: function(){
            console.log("Error while opening up the menu from landing page")
        }
    })
}