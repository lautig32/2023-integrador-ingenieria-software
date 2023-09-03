//accion bnt_login
document.getElementById("btn_login").addEventListener("click", function() {
  var username = document.getElementById("username").value;
  var password = document.getElementById("password").value;
  
  if (username === "usuario" && password === "contraseña") {
    alert("Inicio de sesión exitoso.");
  } else {
    alert("Usuario o contraseña incorrectos.");
  }
});

//validar nombre de usuario
function validateUsername(){
  var usernameInput = document.getElementById("username");
  var usernameError = document.getElementById("username_error");
  
  
  if(usernameInput.value == link.value){
    usernameError.style.display = "El nombre de usuario ya existe.";
  }
  else{
    usernameError.style.display = "none";
  }
}


//validar contraseña del singup
var passwordInput = document.getElementById("password");
var confirmPasswordInput = document.getElementById("confirm_password");
var passwordError = document.getElementById("password_error");

confirmPasswordInput.addEventListener("input", validatePassword);

function validatePassword() {
  if (passwordInput.value !== confirmPasswordInput.value) {
    confirmPasswordInput.setCustomValidity("Las contraseñas no coinciden.");
  } else {
    confirmPasswordInput.setCustomValidity("");
  }
}
passwordInput.addEventListener("input", validatePasswords);


//accion bnt_signup
document.getElementById("signupBtn").addEventListener("click", function() {
  var email = document.getElementById("email").value;
  var username = document.getElementById("user_name").value;
  var password = document.getElementById("password").value;
  var confirm_password = document.getElementById("confirm_password").value;

  if (username && password) {
    alert("Usuario registrado exitosamente.");
  } else {
    alert("Por favor, completa todos los campos.");
  }
});


//js para visualizar contraseña
const passwordInput = document.querySelector(" pass-field input");
const eyeIcon = document .querySelector(" pass-field i");
const requirementList = document.querySelectorAll(".requirement-list li");

const requirements = [
  { regex: /.{8,}/, index: 0 }, // Minimum of 8 characters
]

passwordInput.addEventListener("keyup", (e) => {
  requirements.forEach(item => {
      // Check if the password matches the requirement regex
      const isValid = item.regex.test(e.target.value);
      const requirementItem = requirementList[item.index];

      // Updating class and icon of requirement item if requirement matched or not
      if (isValid) {
          requirementItem.classList.add("valid");
          requirementItem.firstElementChild.className = "fa-solid fa-check";
      } else {
          requirementItem.classList.remove("valid");
          requirementItem.firstElementChild.className = "fa-solid fa-circle";
      }
  });
});

eyeIcon.addEventListener("click", () => {
  passwordInput.type = passwordInput.type === "password" ? "text" : "password";
  eyeIcon.className = `fa-solid fa-eye${passwordInput.type === "password" ? "" : "-slash"}`;
});