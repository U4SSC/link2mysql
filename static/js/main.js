$(window).scroll(function() {
    var scrollTop = $(window).scrollTop();
    if(scrollTop > $("#aboutus").offset().top-10 || scrollTop > $("#aboutus").offset().top-10){
        $(".top_bar").css({"visibility":"hidden"});
    }else if(scrollTop > $("#KPI").offset().top || scrollTop > $("#KPI").offset().top){
        $(".top_bar").addClass("top_bar_toggle");
        $(".top_bar").css({"visibility":"visible"});
    }else{
        $(".top_bar").removeClass("top_bar_toggle");
        $(".top_bar").css({"visibility":"visible"});
    }
});

let slidesNum = 1;
function showSlides(n, _graph) {
    let i;
    let slides = $(_graph+" .slide");
    let dots = $(_graph+" .dot");
    if(n > slides.length){
        slidesNum = 1
    }
    if(n < 1){
        slidesNum = slides.length
    }
    for (i = 0; i < slides.length; i++) {
      slides[i].style.display = "none";
    }
    for (i = 0; i < dots.length; i++) {
      dots[i].className = dots[i].className.replace(" active", "");
    }
    slides[slidesNum-1].style.display = "block";
    dots[slidesNum-1].className += " active";
}

$(".icon_for_graph").click(function() {
    var type = $(this).attr('id');
    var graph = "#"+type+"_img";

    $(graph).addClass("show");

    slidesNum = 1;
    showSlides(slidesNum,graph);

    $(graph+" .prev").click(function() {
        showSlides(slidesNum -= 1,graph);
    });
    $(graph+" .next").click(function() {
        showSlides(slidesNum += 1,graph);
    });
    $(graph+" .dot").click(function() {
        let tmp = $(this).attr("class").split(" ")[1].split('_')[1];
        showSlides(slidesNum = tmp,graph);
    });

    $(".slide").click(function() {
        $(graph).removeClass("show");
    });
});

var checkedCountry = [];

$("#linechartSearch").click(function() {
    checkedCountry = [];
    $("input[type='checkbox']").each(function(){
        if($(this).prop("checked")){
            var name = $(this).attr('id');
            checkedCountry.push(name);
        }
    })
    var json_country = JSON.stringify(checkedCountry);
    console.log(json_country);

    $.ajax({
        type: "POST",
        url: "/create_2d_plot",
        data: json_country,
        contentType: "application/json",
        processData: false,
        dataType: "json",
        success: function(data){
            console.log(data);
            $("#linechart").attr("src", "/static/img/2d_plot.png?timestamp=" + new Date().getTime());
        }
    });
});

$("#linechartClear").click(function() {
    $('input[type=checkbox]').prop('checked',false);
});