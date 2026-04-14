$(function(){

	$(".navbar a, footer a").on("click", function(event){

		event.preventDefault();
		var hash = this.hash;
		if (!hash) return;

		var target = $(hash);
		if (!target.length) return;

		$('body,html').animate({scrollTop: target.offset().top}, 1000, function(){
			window.location.hash = hash;
		});

	});


	$('#contact-form').submit(function(e){
		e.preventDefault();
		$('.comments').empty();
		var postdata = $('#contact-form').serialize();

		$.ajax({
			type: 'POST',
			url: 'php/contact.php',
			data: postdata,
			dataType: 'json',
			success: function(result) {
				if(result.isSuccess) {
					$("#contact-form").append("<p class='thank-you'>Votre message a bien ete envoye. Merci de m'avoir contacte </p>");
					$('#contact-form')[0].reset();
				}
				else {
					$("#firstname + .comments").html(result.firstnameError);
					$("#name + .comments").html(result.nameError);
					$("#email + .comments").html(result.emailError);
					$("#phone + .comments").html(result.phoneError);
					$("#message + .comments").html(result.messageError);
				}
			},
			error: function() {
				$("#contact-form").append("<p class='text-danger'>Une erreur est survenue. Veuillez réessayer plus tard.</p>");
			}
		});

	});

});