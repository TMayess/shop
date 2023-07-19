const titre = document.getElementById("change");
const imgSlide = document.getElementById("img-slide");
const sectionSlide = document.querySelector(".section-slide");
const textSlide = document.querySelector(".text-slide");
const dots = document.querySelectorAll(".dot");

const titre_list = ["Plongez dans un océan de c", "Plongez dans un océan de couleurs !", "Plongez dans un océan de couleurs !"];
const text_list = ["Explorez notre large gamme de vêtements aux couleurs éclatantes. Exprimez-vous avec style et originalité !",
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur blanditiis impedit, rem praesentium quas nobis natus. Praesentium consectetur facilis eum fuga sed expedita repudiandae harum itaque quasi dolor? Reiciendis, in.",
    "Lorem ipsum dolor sit amet consectetur adipisicing elit. Tenetur blanditiis impedit, rem praesentium quas nobis natus. Praesentium consectetur facilis eum fuga sed expedita repudiandae harum itaque quasi dolor? Reiciendis, in."];
const color_list = ["#FFCC00", "#336699", "#993366"];
const image_list = ["image/Logo.PNG", "image/favoris-icone2.png", "image/panier-icone.png"];

let i = 0;

function nextSlide() {
    i = (i + 1) % titre_list.length;

    sectionSlide.style.backgroundColor = color_list[i];
    imgSlide.src = image_list[i];
    dots[(i - 1 + titre_list.length) % titre_list.length].classList.remove("active");


    titre.classList.remove("swipe-in-reverse");
    titre.classList.remove("swipe-in");
    titre.classList.add("swipe-out");

    textSlide.classList.remove("fade-in");
    textSlide.classList.add("fade-out");

    setTimeout(function () {
        textSlide.innerHTML = text_list[i];
        titre.innerHTML = titre_list[i];

        titre.classList.remove("swipe-out");
        void titre.offsetWidth;
        titre.classList.add("show", "swipe-in");
        textSlide.classList.remove("fade-out");
        textSlide.classList.add("fade-in");

        dots[i].classList.add("active");
    }, 250);
}


function prevSlide() {
    i = (i - 1 + titre_list.length) % titre_list.length;

    sectionSlide.style.backgroundColor = color_list[i];
    imgSlide.src = image_list[i];
    dots[(i + 1) % titre_list.length].classList.remove("active");

    titre.classList.remove("swipe-in");
    titre.classList.remove("swipe-in-reverse");
    titre.classList.add("swipe-out-reverse");

    textSlide.classList.remove("fade-in");
    textSlide.classList.add("fade-out");


    setTimeout(function () {
        textSlide.innerHTML = text_list[i];
        titre.innerHTML = titre_list[i];

        titre.classList.remove("swipe-out-reverse");
        void titre.offsetWidth;
        titre.classList.add("swipe-in-reverse");
        textSlide.classList.remove("fade-out");
        textSlide.classList.add("fade-in");

        dots[i].classList.add("active");

    }, 250);
}



const rangeInput = document.querySelectorAll(".range-input input"),
    priceInput = document.querySelectorAll(".price-input input"),
    range = document.querySelector(".slider .progress");
let priceGap = 1000;

priceInput.forEach((input) => {
    input.addEventListener("input", (e) => {
        let minPrice = parseInt(priceInput[0].value),
            maxPrice = parseInt(priceInput[1].value);

        if (maxPrice - minPrice >= priceGap && maxPrice <= rangeInput[1].max) {
            if (e.target.className === "input-min") {
                rangeInput[0].value = minPrice;
                range.style.left = (minPrice / rangeInput[0].max) * 100 + "%";
            } else {
                rangeInput[1].value = maxPrice;
                range.style.right = 100 - (maxPrice / rangeInput[1].max) * 100 + "%";
            }
        }
    });
});

rangeInput.forEach((input) => {
    input.addEventListener("input", (e) => {
        let minVal = parseInt(rangeInput[0].value),
            maxVal = parseInt(rangeInput[1].value);

        if (maxVal - minVal < priceGap) {
            if (e.target.className === "range-min") {
                rangeInput[0].value = maxVal - priceGap;
            } else {
                rangeInput[1].value = minVal + priceGap;
            }
        } else {
            priceInput[0].value = minVal;
            priceInput[1].value = maxVal;
            range.style.left = (minVal / rangeInput[0].max) * 100 + "%";
            range.style.right = 100 - (maxVal / rangeInput[1].max) * 100 + "%";
        }
    });
});


let subMenu = document.getElementById("droplist");
    function toggleMenu(){
        subMenu.classList.toggle("open-menu");
    }