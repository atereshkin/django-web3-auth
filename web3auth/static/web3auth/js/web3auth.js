web3auth = {

    init : function(loginToken) {
	$(() => {
	    if (typeof web3 !== 'undefined') {
		web3 = new Web3(web3.currentProvider);
		web3.eth.getAccounts((err, accounts) => { // Check for wallet being locked
		    if (err) {
			throw err;
		    }
		    if (accounts.length == 0) {
			$('[data-web3auth-display').hide();
			$('[data-web3auth-display="wallet-locked"]').show();
		    } else {
			$('[data-web3auth-display').hide();
			$('[data-web3auth-display="wallet-available"]').show();
		    }
		    
		});
	    } else {
		$('[data-web3auth-display').hide();
		$('[data-web3auth-display="wallet-unavailable"]').show();
	    }
	    
	});
	let loginBtn = $('[data-web3auth="login-button"]');
	$(loginBtn).click(() => {
	    web3auth.login(loginToken, $('[data-web3auth="login-form"]'));
	    return false;
	});
	
    },
    
    login : function(loginToken, form){
	if (typeof web3 == 'undefined') {
	    throw 'web3 missing';
	}	
	msg=web3.toHex(loginToken);
	from = web3.eth.accounts[0];
	web3.personal.sign(msg, from, (err, result) => {
	    if (err){
		console.log(err, result);
	    } else {
		$(form).find('input[name=signature]').val(result);
		$(form).submit();
	    }
	});

    }
}
