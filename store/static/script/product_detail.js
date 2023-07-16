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