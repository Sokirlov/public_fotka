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
        // desctop jquery GAllery
       var galLen = $(".gallerys .gallPhoto").length
        if (galLen % 3 == 0){
            $('.gallPhoto').each(function() {
                $(this).attr('style', 'width: calc((100% / 3) - 8px)')
            });
        } else if(galLen % 4 == 0){
            $('.gallPhoto').each(function() {
                $(this).attr('style', 'width: calc((100% / 4) - 8px)')
            });
        }else{
            $('.gallPhoto').each(function() {
                $(this).attr('style', 'width: calc((100% / 3) - 8px)')
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
//  -----  youtube img src to video

    $(function() {
        $(".youtube").each(function() {
            // Based on the YouTube ID, we can easily find the thumbnail image
            $(this).css('background-image', 'url(http://i.ytimg.com/vi/' + this.id + '/hqdefault.jpg)');

            // Overlay the Play icon to make it look like a video player
            $(this).append($('<div/>', {'class': 'play'}));

            $(document).delegate('#'+this.id, 'click', function() {
                // Create an iFrame with autoplay set to true
                var iframe_url = "https://www.youtube.com/embed/" + this.id + "?autoplay=1&autohide=1";
                if ($(this).data('params')) iframe_url+='&'+$(this).data('params');

                // The height and width of the iFrame should be the same as parent
                var iframe = $('<iframe/>', {'frameborder': '0', 'src': iframe_url, 'width': $(this).width(), 'height': $(this).height() })

                // Replace the YouTube thumbnail with YouTube HTML5 Player
                $(this).replaceWith(iframe);
            });
        });
    });

});