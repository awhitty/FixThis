function refreshPage() {
				$('#login-form').hide()
			$('#register-form').hide()

			$('#login-button').click(function(e) {
				$('#login-buttons a').removeClass('ui-btn-active')
				$(this).addClass('ui-btn-active')
				$('#login-form').show()
				$('#register-form').hide()
			})

			$('#register-button').click(function(e) {
				$('#login-buttons a').removeClass('ui-btn-active')
				$(this).addClass('ui-btn-active')
				$('#login-form').hide()
				$('#register-form').show()
			})
}