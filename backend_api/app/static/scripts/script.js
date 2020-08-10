$(".burger").on("click", function () {
    $(".fas, nav").toggleClass("off");
})

$(document).on('scroll', function () {

    const windowHeight = $(window).height()
    const scrollValue = $(this).scrollTop();

    const $art1 = $('.art1');
    const art1FromTop = $art1.offset().top
    const art1Height = $art1.outerHeight()

    const $art2 = $('.art2');
    const art2FromTop = $art2.offset().top
    const art2Height = $art2.outerHeight()

    const $art3 = $('.art3');
    const art3FromTop = $art3.offset().top
    const art3Height = $art3.outerHeight()

    if (windowHeight <= 736) {
        if (scrollValue > art1FromTop + art1Height - windowHeight - 200) {
            console.log(windowHeight);
            $art1.addClass('active');
        }

        if (scrollValue > art2FromTop + art2Height - windowHeight - 200) {
            $art2.addClass('active');
        }

        if (scrollValue > art3FromTop + art3Height - windowHeight - 200) {
            $art3.addClass('active');
        }
    } else if (windowHeight <= 960) {
        if (scrollValue > art1FromTop + art1Height - windowHeight - 120) {
            console.log(windowHeight);
            $art1.addClass('active');
        }

        if (scrollValue > art2FromTop + art2Height - windowHeight - 120) {
            $art2.addClass('active');
        }

        if (scrollValue > art3FromTop + art3Height - windowHeight - 120) {
            $art3.addClass('active');
        }
    } else if (windowHeight <= 1280) {
        if (scrollValue > art1FromTop + art1Height - windowHeight - 250) {
            console.log(windowHeight);
            $art1.addClass('active');
        }

        if (scrollValue > art2FromTop + art2Height - windowHeight - 250) {
            $art2.addClass('active');
        }

        if (scrollValue > art3FromTop + art3Height - windowHeight - 250) {
            $art3.addClass('active');
        }
    } else {
        if (scrollValue > art1FromTop + art1Height - windowHeight - 100) {
            console.log(windowHeight);
            $art1.addClass('active');
        }

        if (scrollValue > art2FromTop + art2Height - windowHeight - 100) {
            $art2.addClass('active');
        }

        if (scrollValue > art3FromTop + art3Height - windowHeight - 100) {
            $art3.addClass('active');
        }
    }
    if (scrollValue < 100) {
        $('article').removeClass('active');
    }
})