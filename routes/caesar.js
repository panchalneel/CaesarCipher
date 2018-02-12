let express = require('express');
let router = express.Router();
let pain = "DEFGHIJKLMNOPQRSTUVWXYZABC";
let encrypt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
let plainChar = pain.split("");
let encryptChar = encrypt.split("");


/**
 * @description To encrypt message
 * @author Nil Panchal
 * @version 1.0
 */
router.get('/encrypt', function (req, res, next) {
	let text = req.query.message;
	console.log(text);
	let encryptedMessage = "";
	for (let i = 0; i < text.length; i++) {
		if (plainChar.indexOf(text[i].toUpperCase())) {
			encryptedMessage += encryptChar[plainChar.indexOf(text[i].toUpperCase())];
		}
	}
	res.send({status: "Success", encryptedMessage: encryptedMessage});
});


/**
 * @description To decrypt message
 * @author Nil Panchal
 * @version 1.0
 */
router.get('/decrypt', function (req, res, next) {
	console.log(req.query.message);
	let message = req.query.message;
	var decryptedText = "";
	for (let i = 0; i < message.length; i++) {
		if (encryptChar.indexOf(message[i].toUpperCase()) != -1) {
			decryptedText += plainChar[encryptChar.indexOf(message[i].toUpperCase())];
		}
	}
	res.send({status: "Success", decryptedText: decryptedText});
});

module.exports = router;
