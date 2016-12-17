(function(){

    //Вывод Избранного при подключении
    function toggleInformer_1() {
    	if ($.cookie('id') != undefined){
    		if ($.cookie('id') != 0){
        		var xhr = new XMLHttpRequest();
        		var params = 'id=' + encodeURIComponent($.cookie('id'));

        		xhr.open('GET', '/favorite/?'+params, true);
        		xhr.send();

        		xhr.onreadystatechange = function() { // (3)
      				if(xhr.readyState == 4){
        				if (xhr.status != 200) {
      					// обработать ошибку
      						alert( xhr.status + ': ' + xhr.statusText ); // пример вывода: 404: Not Found
    					} else {
      					// вывести результат
      					// responseText -- текст ответа.
      						var foo = document.getElementById('fav');
    						foo.innerHTML = xhr.responseText;
    					}
    				}
    			}
    		}
    	}
    }

    //Удалени из избранного
    $('.close_bl').live('click', function() {
        var id = $(this).attr("id");
        var list = $.cookie('id');
        var arr = list.split(' ');

        arr.forEach(function(item,i,arr){
            if (item == id){
                arr.splice(i,1);  
            }
        });
                
        send = arr.join(' ');
        document.cookie = "id="+send+"; path=/;";

        var block_id = "block_"+id;
        document.getElementById(block_id).style.display = 'none';
    });

    //Отправка формы
    function call() {
        var xhr = new XMLHttpRequest();
        // создать объект для формы
        
        var name = encodeURIComponent(document.getElementsByName('name')[0].value);
        var surname = encodeURIComponent(document.getElementsByName('surname')[0].value);
        var email = encodeURIComponent(document.getElementsByName('email')[0].value);
        var phone = encodeURIComponent(document.getElementsByName('phone')[0].value);
        var time_from = encodeURIComponent(document.getElementsByName('time_from')[0].value); 
        var time_to = encodeURIComponent(document.getElementsByName('time_to')[0].value); 
        var date_from = encodeURIComponent(document.getElementsByName('date_from')[0].value);
        var date_to = encodeURIComponent(document.getElementsByName('date_to')[0].value); 
        var people = encodeURIComponent(document.getElementsByName('people')[0].value); 
        var child_5 = encodeURIComponent(document.getElementsByName('child_5')[0].value); 
        var child_12 = encodeURIComponent(document.getElementsByName('child_12')[0].value); 
        var comment = encodeURIComponent(document.getElementsByName('comment')[0].value);
                
        var params = 'name=' + name + '&surname=' + surname + '&email=' + email + '&phone=' + phone + '&time_from=' + time_from + '&time_to=' + time_to + '&date_from=' + date_from + '&date_to=' + date_to + '&people=' + people + '&child_5=' + child_5 + '&child_12=' + child_12 + '&comment=' + comment + '&id=' + $.cookie('id');
        // отослать
        var xhr = new XMLHttpRequest();
        xhr.open("GET", "/callback/?"+params);
        xhr.send();
        xhr.onreadystatechange = function() {
            if(xhr.readyState == 4){
                alert( xhr.responseText );
            }
        }
    }
})();