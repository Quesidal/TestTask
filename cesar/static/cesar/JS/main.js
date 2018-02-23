var delay;


function analys_web() {
    var fade_delay = 400
    if ($("#original_text").val().length > 0) {
        $.getJSON("/analysis/",
            {
                'original_text': $("#original_text").val(),
                'heigh': $("#original_text").height(),
                'width': $("#original_text").width()
            },

            function (msg) {
                if(msg.text.decrypt_text.length > 0) {
                    $(".chart").fadeIn(fade_delay);
                }


                if (msg.text.decrypt_text.length > 0) {
                    $(".info").fadeIn(fade_delay);
                    $("#info_header").text(msg.text.header);
                    $("#rotation").text(msg.text.decrypt_text);
                }
                else {
                    $(".info").fadeOut(fade_delay);
                }

                graph_date = [["Letter", "Frequency", {role: "style"}]];
                freq_dict = msg['freq'];
                letter = Object.keys(freq_dict);
                letter.forEach(function (item, i, arr) {
                    graph_date.push([item, freq_dict[item], "#c6c6c6"]);
                });

                google.charts.load('current', {packages: ['corechart']});
                google.charts.setOnLoadCallback(drawChart);

                function drawChart() {
                    var data = google.visualization.arrayToDataTable(graph_date);


                    var view = new google.visualization.DataView(data);
                    view.setColumns([0, 1, 2]);


                    var options = {
                        width: $('.chart').width(),
                        height: 200,
                        bar: {groupWidth: "25%"},
                        legend: {position: "none"},
                    };
                    var chart = new google.visualization.ColumnChart(document.getElementById("columnchart_values"));
                    chart.draw(view, options);
                }

            })
    }
    else {
        $(".info").fadeOut(fade_delay);
        $(".chart").fadeOut(fade_delay);
    }
}


$(window).resize(function () {
    analys_web();
});


$(document).ready(function () {
    setTimeout(function () {
        analys_web();
    }, 1000);
});


$("#original_text").keyup(function () {
    clearTimeout(delay);

    delay = setTimeout(function () {
        analys_web();
    }, 10);
});


$('#btn_crypt').click(function () {
    if (!isNaN($("#rot").val())) {
        $('.error').fadeOut();
        $.getJSON("/crypt/",
            {
                'text': $("#original_text").val(),
                'rot': $("#rot").val()
            },

            function (msg) {
                console.log(msg.crypt_text)
                $('#crypt_text').text(msg.crypt_text)
            });

    }
    else {
        $('.error').fadeIn('Slow');
    }
});


$('#btn_crypt').focusout(function () {
    $('.error').fadeOut();
});


$('#btn_decrypt').click(function () {
    if (!isNaN($("#rot").val())) {
        $('.error').fadeOut();
        $.getJSON("/decrypt/",
            {
                'text': $("#original_text").val(),
                'rot': $("#rot").val()
            },

            function (msg) {
                $('#crypt_text').text(msg.info_decrypt)
            });
    }
    else {
        $('.error').fadeIn('Slow');
    }
});


$('#btn_decrypt').focusout(function () {
    $('.error').fadeOut();
});