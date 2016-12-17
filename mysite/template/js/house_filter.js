(function(){
    $( "#money" ).slider({
        animate: true,
        range: true,
        values: [0, 10000],
        min: 0,
        max: 10000,
        step: 50,
        //Получаем значение и выводим его на странице

        slide: function( event, ui ) {
          $( "#money-left" ).html( ui.values[0] );
          $( "#money-right" ).html( ui.values[1] );
        },
        //Обновляем скрытое поле формы, так что можно передать данные с помощью формы
        change: function(event, ui) {
          $('#money-left_input').attr('value', ui.values[0]);
          $('#money-right_input').attr('value', ui.values[1]);
        }
    });

     $( "#sea" ).slider({
        animate: true,
        range: true,
        values: [0, 2000],
        min: 0,
        max: 2000,
        step: 10,
        //Получаем значение и выводим его на странице

        slide: function( event, ui ) {
          $( "#sea-left" ).html( ui.values[0] );
          $( "#sea-right" ).html( ui.values[1] );
        },
        //Обновляем скрытое поле формы, так что можно передать данные с помощью формы
        change: function(event, ui) {
          $('#sea-left_input').attr('value', ui.values[0]);
          $('#sea-right_input').attr('value', ui.values[1]);
        }
    });	
})();