const signForms = document.querySelectorAll('.sign-form');
const container = document.querySelector('.container');

let currentIndex = 0;
const formWidth = signForms[0].offsetWidth;
console.log(currentIndex)

function scrollLeftPerso() {
  if (currentIndex > 0) {
    currentIndex--;
    console.log(currentIndex)

    container.style.transform = `translateX(-${currentIndex * formWidth}px)`;
  }
}

function scrollRight() {
  const errors = document.querySelectorAll(".sign-form .error");
  let hasError = false;
  const fields = [
    {
      id: "lastname",
      errorIndex: 0,
      errorMessage: "Veuillez fournir votre nom.",
    },
    {
      id: "firstname",
      errorIndex: 1,
      errorMessage: "Veuillez fournir votre prénom.",
    },
    {
      id: "birthdate",
      errorIndex: 2,
      errorMessage: "Veuillez sélectionner votre date de naissance.",
    },
  ];

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

  if (hasError) {
    return;
  }

  if (currentIndex < signForms.length - 1) {
    currentIndex++;
    container.style.transform = `translateX(-${currentIndex * formWidth}px)`;
  }
}