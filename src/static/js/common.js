$(document).ready(function(){
    $('.tooltipped').tooltip();
    $(".dropdown-trigger").dropdown({
        hover: true,         // Trigger down-down on hover
        coverTrigger: false  // Don't cover element that triggered drop-down, i.e. display drop-down beneath element
    });
});
