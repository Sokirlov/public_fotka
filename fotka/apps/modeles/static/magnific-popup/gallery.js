$(document).ready(function() {
    $('.gallerys.blocks').magnificPopup({
        delegate: '.gallpopup', // child items selector, by clicking on it popup will open
        type: 'image',
        // other options
        gallery: {
            enabled: true
        }
    });
    $('.popup-youtube').magnificPopup({
        disableOn: 700,
        type: 'iframe',
        mainClass: 'mfp-fade',
        removalDelay: 160,
        preloader: True,

        fixedContentPos: false
    });

});

// function extendMagnificIframe(){
//
//     var $start = 0;
//     var $iframe = {
//         markup: '<div class="mfp-iframe-scaler">' +
//                 '<div class="mfp-close"></div>' +
//                 '<iframe class="mfp-iframe" frameborder="0" allowfullscreen></iframe>' +
//                 '</div>' +
//                 '<div class="mfp-bottom-bar">' +
//                 '<div class="mfp-title"></div>' +
//                 '</div>',
//         patterns: {
//             youtube: {
//                 index: 'youtu',
//                 id: function(url) {
//                     var m = url.match( /^.*(?:youtu.be\/|v\/|e\/|u\/\w+\/|embed\/|v=)([^#\&\?]*).*/ );
//                     if ( !m || !m[1] ) return null;
//                         if(url.indexOf('t=') != - 1){
//                             var $split = url.split('t=');
//                             var hms = $split[1].replace('h',':').replace('m',':').replace('s','');
//                             var a = hms.split(':');
//                             if (a.length == 1){
//                                 $start = a[0];
//                             } else if (a.length == 2){
//                                 $start = (+a[0]) * 60 + (+a[1]);
//                             } else if (a.length == 3){
//                                 $start = (+a[0]) * 60 * 60 + (+a[1]) * 60 + (+a[2]);
//                             }
//                         }
//                         var suffix = '?autoplay=1';
//                         if( $start > 0 ){
//                             suffix = '?start=' + $start + '&autoplay=1';
//                         }
//                     return m[1] + suffix;
//                 },
//                 src: '//www.youtube.com/embed/%id%'
//             },
//         }
//     };
//
//     return $iframe;
//
// }
//
// $('.popup-youtube').magnificPopup({
//     type: 'iframe',
//     iframe: extendMagnificIframe()
// });