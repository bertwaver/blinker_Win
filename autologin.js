var usernameInput = document.querySelector("input[name=\'username\']");
var passwordInput = document.querySelector("input[name=\'password\']");
var usernameValue = "usename";
var passwordValue = "password";
var usernameEvent = new Event("input", { bubbles: true });
var passwordEvent = new Event("input", { bubbles: true });
usernameInput.value = usernameValue;
usernameInput.dispatchEvent(usernameEvent);
passwordInput.value = passwordValue;
passwordInput.dispatchEvent(passwordEvent);