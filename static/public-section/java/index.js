//script for adding color to the menu
    $(document).ready(function () {
        $("#mobileMenuIcon").click(function () {
            $("#mobileMenuIcon").hide();
            $("#mobileMenuCloseIcon").css("display","block");
            $("#header").addClass("active");
        });

        $("#mobileMenuCloseIcon").click(function () {
            $("#mobileMenuIcon").show();
            $("#mobileMenuCloseIcon").hide();
        });

        $(".header-section").click(function () {
            $("#header").removeClass("active");
        });



    });




/* Fucntion shows border box shadow on scroll on nav bar */
$(window).scroll(function() {
    var scroll = $(window).scrollTop();
    if (scroll > 0) {
        $("#header").addClass("active");
    }
    else {
        $("#header").removeClass("active");
    }
});
/* End of Fucntion which shows border box shadow on scroll on nav bar */









    /* function to show arrow up button on 20% scroll */
myscrollUp=document.getElementById("myScrollUp");
window.onscroll= function (){scrollFunction()};





function scrollFunction(){
    if(document.body.scrollTop > 20 || document.documentElement.scrollTop > 20 ){

       myscrollUp.style.display="block";
    }
    else {
        myscrollUp.style.display="none";
    }
}
function funtop(){
    document.body.scrollTop=0;
    document.documentElement.scrollTop=0;
}
/*End of function to show arrow up button on 20% scroll */