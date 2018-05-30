$(document).ready(function() {

	$('form').on('submit', function(event) {

		$.ajax({
			data : {
				name : $('#user_name').val()
			},
			type : 'POST',
			url : '/run'
		})
		.done(function(data) {

			if(data.result1){
				$('#result1').text(data.result1).show();
			}
			if(data.result2){
				$('#result2').text(data.result2).show();
			}
			if(data.result3){
				$('#result3').text(data.result3).show();
			}
			if(data.result4){
				$('#result4').text(data.result4).show();
			}
			if(data.result5){
				$('#result5').text(data.result5).show();
			}
			if(data.result6){
				$('#result6').text(data.result6).show();
			}
			if(data.result7){
				$('#result7').text(data.result7).show();
			}
			if(data.result8){
				$('#result8').text(data.result8).show();
			}
			
			else{
				$('#errorAlert').text(data.error).show();
			}

		});

		event.preventDefault();

	});

});