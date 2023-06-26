//accion bnt_login
document.getElementById("btn_login").addEventListener("click", function() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  
  if (username === "usuario" && password === "contraseña") {
    alert("Inicio de sesión exitoso");
  } else {
    alert("Usuario o contraseña incorrectos");
  }
});


//validar contraseña del singup
var passwordInput = document.getElementById("password");
var confirmPasswordInput = document.getElementById("confirm_password");
var passwordError = document.getElementById("password_error");

function validatePassword() {
  if (passwordInput.value !== confirmPasswordInput.value) {
      passwordError.style.display = "block";
  } else {
      passwordError.style.display = "none";
  }
}
confirmPasswordInput.addEventListener("input", validatePassword);

//accion bnt_signup
document.getElementById("signupBtn").addEventListener("click", function() {
  var email = document.getElementById("email").value;
  var username = document.getElementById("user_name").value;
  var password = document.getElementById("password").value;
  var confirm_password = document.getElementById("confirm_password").value;

  if (username && password) {
    alert("Usuario registrado exitosamente");
  } else {
    alert("Por favor, completa todos los campos");
  }
});
