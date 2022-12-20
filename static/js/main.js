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

$(".icon_for_graph").click(function() {
    var type = $(this).attr('id');
    var graph = "#"+type+"_img";

    $(graph).addClass("show");
    $(graph).click(function() {
        $(graph).removeClass("show");
        $("body").removeClass("disable_scroll");
    });
});