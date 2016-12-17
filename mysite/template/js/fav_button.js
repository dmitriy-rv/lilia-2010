(function(){    						
    //Событие при нажатии кнпки избранное
    function toggleInformer(){ 	
        if ($.cookie('id') == undefined){
        	document.cookie = "id={{ article.id }}";
        	$( "#test" ).html(1);
            document.getElementById('favor').innerText = 'В Избранном';
            document.getElementById('favor').style = 'background: white; color:#070849;';	
        }else{
        	var list = $.cookie('id');
        	var arr = list.split(' ');

            var enable = 1;
        							
        	arr.forEach(function(item,i,arr){
        		if (item == {{ article.id }}){
        			enable = 0;
        		}
        	});

            if (enable == 1){
            	arr[arr.length] = {{ article.id }};
            	send = arr.join(' ');
            	document.cookie = "id="+send;
            	document.getElementById('favor').innerText = 'В Избранном';
            	document.getElementById('favor').style = 'background: white; color:#070849;';
            }
        							
        	$( "#test" ).html( arr.length );
        }
    }
    //Событие при загрузки страницы
    jQuery(document).ready(function(){   
                			             
    	if ($.cookie('id') == undefined){
    		var fav_num = 0;
    	}else{
    		var list = $.cookie('id');
        	var arr = list.split(' ');
        							
        	arr.forEach(function(item,i,arr){
        		if (Number(item) == {{ article.id }}){
        			document.getElementById('favor').innerText = 'В Избранном';
        			document.getElementById('favor').style = 'background: white; color:#070849;';
        		}
        	});

        	$( "#test" ).html( arr.length );
    	}
    });
})();
