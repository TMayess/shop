    $(function () {

        var inWrap = $('.inner-wrapper');
        var slides2 = $('.slide2');
        var slideWidth = $('.slide').outerWidth();

        let i = 0;

        $('.a-prev').on('click', function () {
            $('.slide').last().insertBefore($('.slide').first());
            inWrap.css('left', -slideWidth);
            inWrap.animate({ left: 0 }, 300);
            i = (i - 1 + slides2.length) % slides2.length;

            updateOpacity(i);
        });



        $('.a-next').on('click', function () {

            inWrap.animate({ left: -slideWidth }, 300, function () {

                inWrap.css('left', '0%');

                $('.slide').last().after($('.slide').first());

                i = (i + 1) % slides2.length;

                updateOpacity(i);

            });


        });

        function updateOpacity(i) {
            slides2.css('opacity', '0.5');
            slides2.eq(i).css('opacity', '1');
        }
        updateOpacity(i);


    })


    document.addEventListener("DOMContentLoaded", function() {
    const colorOptions = document.querySelectorAll(".color-option");
    const tailleList = document.getElementById("list-taille");


    function updateTailleList(sizes) {
        tailleList.innerHTML = "";
        sizes.forEach((size, index) => {
            const li = document.createElement("li");
            li.textContent = size.toUpperCase();
            tailleList.appendChild(li);

            if (index === 0) {
                li.classList.add("active");
            }

            li.addEventListener("click", function() {
                // Supprimer la classe "active" de tous les autres éléments li
                const allLiElements = tailleList.querySelectorAll("li");
                allLiElements.forEach(element => element.classList.remove("active"));

                // Ajouter la classe "active" à l'élément li cliqué
                this.classList.add("active");
            });

        });
    }

    //colorOptions[0].classList.add("active");


    const selectedSizes = eval(colorOptions[0].dataset.sizes);
    updateTailleList(selectedSizes);

    // Gestionnaire d'événement de clic pour les options de couleur
    colorOptions.forEach(colorOption => {
        colorOption.addEventListener("click", function() {
            const selectedSizes = eval(this.dataset.sizes);
            console.log(selectedSizes);
            updateTailleList(selectedSizes);
            colorOptions.forEach(option => option.classList.remove("active"));
            this.classList.add("active");
        });
    });
});