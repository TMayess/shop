const signForms = document.querySelectorAll('.sign-form');
const container = document.querySelector('.container');

let currentIndex = 0;
const formWidth = signForms[0].offsetWidth;
console.log(currentIndex)

function scrollLeftPerso() {
  if (currentIndex > 0) {
    currentIndex--;
    container.style.transform = `translateX(-${currentIndex * formWidth}px)`;
  }
}

function scrollRight() {
  const errors = document.querySelectorAll(".sign-form .error");

/*
  fields.forEach((field) => {
    const inputField = document.getElementById(field.id);
    const error = errors[field.errorIndex];
    const errorText = error.querySelector(".error-text");

    if (inputField.value.trim() === "") {
      hasError = true;
      errorText.textContent = field.errorMessage;
      error.style.display = "flex";
    } else {
      error.style.display = "none";
    }
  });
*/
  /*if (hasError) {
    return;
  }*/

  if (currentIndex < signForms.length - 1) {
    currentIndex++;
    container.style.transform = `translateX(-${currentIndex * formWidth}px)`;
  }
}