$(document).ready(function() {
namespace = '/test'; //main.pyで指定したnamespace
var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port + namespace);

//テキストエリアはこちらで受信。main.py側からmy_content宛に送られたデータを受け取る
socket.on('my_content', function(msg) {
    $(".row").append('<div class="col-xs-12 col-sm-4"><div class="card"><a class="img-card" href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E6%88%90"><img src="./images/heisei.jpg" /></a><div class="card-content"><h4 class="card-title"><a href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E6%88%90">' + msg.data + '</a></h4><table  class="t12 font12"><tr><td class="table-title">ジャンル</td><td>：</td><td class="genre">'+msg.data2+'</td></tr><tr><td class="table-title">日付</td><td>：</td><td class="date">1998/03/22</td></tr></table></div><div class="card-read-more"><a href="https://ja.wikipedia.org/wiki/%E5%B9%B3%E6%88%90" class="btn btn-link btn-block">Read More</a></div></div></div>'); // <div id="place"></div>内に、受け取ったdataを挿入します。
});

//htmlのフォームがsubmitされた時に、main.pyのreceive_content宛にテキストエリアのid="input_data"の値を送信します。
$('form#broadcast').submit(function(event) {
    socket.emit('my_broadcast_event', {data: $('#broadcast_data').val(),data2:$('#broadcast_data2').val()});
    console.log("protocol" + ':' + location.protocol);
    console.log("domain" + ':' + document.domain);
    console.log("port" + ':' + location.port);
    return false;
});

});