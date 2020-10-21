$(document).ready(function() {
//---------- galler ordering
    if (/Android|webOS|iPhone|iPad|iPod|BlackBerry|IEMobile|Opera Mini/i.test(navigator.userAgent)) {
    //    mobile menu
    $('#mob-menu').click(function() {
        if($('#mob-menu').hasClass('gg-close')){
            $('#mob-menu').addClass('gg-menu-right').removeClass('gg-close')
            $('.buttons').attr('style', 'display:none')
            $('.bgr-menu').attr('style', 'display:none')
            return;
        }
        if($('#mob-menu').hasClass('gg-menu-right')) {
            $('#mob-menu').addClass('gg-close').removeClass('gg-menu-right')
            $('.buttons').attr('style', 'display:flex')
            $('.bgr-menu').attr('style', 'display:block')
        }
    });
    $('.bgr-menu').click(function() {
            $('#mob-menu').addClass('gg-menu-right').removeClass('gg-close')
            $('.buttons').attr('style', 'display:none')
            $('.bgr-menu').attr('style', 'display:none')
        });
    }else{
        // desctop jquery
       var galLen = $(".gallerys .gallPhoto").length
        if (galLen % 3 == 0){
            $('.gallPhoto').each(function() {
                $(this).attr('style', 'width: calc((100% / 3) - 6px)')
            });
        } else if(galLen % 4 == 0){
            $('.gallPhoto').each(function() {
                $(this).attr('style', 'width: calc((100% / 4) - 6px)')
            });
        }else{
            $('.gallPhoto').each(function() {
                $(this).attr('style', 'width: calc((100% / 3) - 6px)')
            });
        }
    }
//--------------------- Форма Заказа --------------
    $('.clik_zakaz').click(function() {
        $('.form').attr('style', 'display:flex').addClass('start')
        $('.form_block').addClass('start')
    });
    $('.form_bgr').click(function() {
        $('.form').attr('style', 'display:none').removeClass('start')
        $('.form_block').removeClass('start')
    });
    //--------------------- анимация ------------------
    var windowHeight = $(window).height();
    $('.an').each(function() {  //  ищем этот стиль
        var self = $(this);
        if (self.offset().top < windowHeight) {
            self.addClass('start')
        }
    });
// ------------ modeles form attr for date ------------
    $('#id_birthday_day').attr('required', '');
    $('#id_birthday_month').attr('required', '');
    $('#id_birthday_year').attr('required', '');


    $(document).on('scroll', function() {
        $('.an').each(function() {  //  ищем этот стиль
            var self = $(this),
            height;
            if (self.height() >= windowHeight){
                height = self.offset().top + windowHeight - 200;
            } else {
                height = self.offset().top + self.height() - 200;
            }
            if ($(document).scrollTop() + windowHeight >= height) {
                self.addClass('start')  // дописываем этот стиль
            }
        });
    });

});