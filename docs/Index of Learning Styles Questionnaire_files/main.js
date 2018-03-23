/* ========================================================================
 * DOM-based Routing
 * Based on http://goo.gl/EUTi53 by Paul Irish
 *
 * Only fires on body classes that match. If a body class contains a dash,
 * replace the dash with an underscore when adding it to the object below.
 *
 * .noConflict()
 * The routing is enclosed within an anonymous function so that you can
 * always reference jQuery with $, even when in .noConflict() mode.
 * ======================================================================== */

(function($) {

    // Use this variable to set up the common and page specific functions. If you
    // rename this variable, you will also need to rename the namespace below.
    var Sage = {
        // All pages
        'common': {
            init: function() {
                // JavaScript to be fired on all pages

            },
            finalize: function() {
                // JavaScript to be fired on all pages, after page specific JS is fired
                var bumpIt = function() {
                        $('#content-body').css('margin-bottom', $('footer.content-info').height());
                    },
                    didResize = false;

                bumpIt();

                $(window).resize(function() {
                    didResize = true;
                });
                setInterval(function() {
                    if(didResize) {
                        didResize = false;
                        bumpIt();
                    }
                }, 100);

                $(".main-menu li.show-children").append("<div class=\"indicator\"></div>");

                var stickyNav = function(stickyNavTop, navHeaderHeight){
                    var scrollTop = $(window).scrollTop();

                    if($('body').hasClass('admin-bar')) {
                        scrollTop += 30;
                    }

                    if (scrollTop >= stickyNavTop) {
                        $('.nav-wrapper').addClass('sticky');
                    } else {
                        $('.nav-wrapper').removeClass('sticky');
                        if(document.documentElement.clientWidth > 990) {
                            $('.nav-header').css({"height": navHeaderHeight});
                        }
                    }
                };


                $(window).on("load", function(){
                    if ($('.nav-wrapper').length) {
                        window.stickyNavTop = $('.nav-wrapper').offset().top;
                    }
                    window.navHeaderHeight = $('.main-nav').outerHeight(true) + $('.main-sub-nav').height() + $('.mobile-nav').height();
                    window.backToTopOffset = $('.page-main-content').offset().top;
                    window.backToTopDuration = 500;
                    if(document.documentElement.clientWidth > 990) {
                        stickyNav(window.stickyNavTop, window.navHeaderHeight);
                    }
                });


                $(window).scroll(function() {
                    if(document.documentElement.clientWidth > 990) {
                        stickyNav(window.stickyNavTop, window.navHeaderHeight);
                    }
                    window.backToTopOffset = $('.page-main-content').offset().top;
                    if ($(this).scrollTop() > backToTopOffset) {
                        $('.back-to-top').fadeIn(window.backToTopDuration);
                    } else {
                        $('.back-to-top').fadeOut(window.backToTopDuration);
                    }
                });

                $('.back-to-top').click(function(event) {
                    event.preventDefault();
                    $(this).css('background', 'rgba(253, 215, 38, .8)');
                    $(this).css('text-decoration', 'none');
                    $('html, body').animate({scrollTop: 0}, window.backToTopDuration);
                    return false;
                });
            }
        },
        // Home page
        'home': {
            init: function() {
                // JavaScript to be fired on the home page
            },
            finalize: function() {
                // JavaScript to be fired on the home page, after the init JS
            }
        }
    };

    // The routing fires all common scripts, followed by the page specific scripts.
    // Add additional events for more control over timing e.g. a finalize event
    var UTIL = {
        fire: function(func, funcname, args) {
            var fire;
            var namespace = Sage;
            funcname = (funcname === undefined) ? 'init' : funcname;
            fire = func !== '';
            fire = fire && namespace[func];
            fire = fire && typeof namespace[func][funcname] === 'function';

            if (fire) {
                namespace[func][funcname](args);
            }
        },
        loadEvents: function() {
            // Fire common init JS
            UTIL.fire('common');

            // Fire page-specific init JS, and then finalize JS
            $.each(document.body.className.replace(/-/g, '_').split(/\s+/), function(i, classnm) {
                UTIL.fire(classnm);
                UTIL.fire(classnm, 'finalize');
            });

            // Fire common finalize JS
            UTIL.fire('common', 'finalize');
        }
    };

    // Load Events
    $(document).ready(UTIL.loadEvents);

})(jQuery);