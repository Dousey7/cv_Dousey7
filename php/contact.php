<?php

	$array = array('firstname' => "", 'name' => "", 'email' => "", 'phone' => "", 'message' => "", 'firstnameError' => "", 'nameError' => "", 'emailError' => "", 'phoneError' => "", 'messageError' => "", 'isSuccess' => false);

	$emailTo = "seydaw7@gmail.com";

	if ($_SERVER["REQUEST_METHOD"] == "POST")
	{
		$array["firstname"] = verifyInput($_POST["firstname"]);
		$array["name"] = verifyInput($_POST["name"]);
		$array["email"] = verifyInput($_POST["email"]);
		$array["phone"] = verifyInput($_POST["phone"]);
		$array["message"] = verifyInput($_POST["message"]);
		$array["isSuccess"] = true;
		$emailText = "";

		if (empty($array["firstname"])) {
			$array["firstnameError"] = "Je veux connaitre ton prénom !";
			$array["isSuccess"] = false;

		}
		else {
			$emailText .= "FirstName: {$array["firstname"]}\n";
		}

		if (empty($array["name"])) {
			$array["nameError"] = "Et oui je veux tout savoir. Meme ton nom !";
			$array["isSuccess"] = false;

		}
		else {
			$emailText .= "Name: {$array["name"]}\n";
		}

		if (empty($array["message"])) {
			$array["messageError"] = "Que voulez-vous me dire S'il vous plait ?!";
			$array["isSuccess"] = false;

		}
		else {
			$emailText .= "Message: {$array["message"]}\n";
		}

		if (!isEmail($array["email"])) {
			$array["emailError"] = "T'essaies de me rouler ? C'est pas un email ca !";
			$array["isSuccess"] = false;

		}
		else {
			$emailText .= "Email: {$array["email"]}\n";
		}

		if(!isPhone($array["phone"])) {
			$array["phoneError"] = "Que des chiffres et des espaces ...";
			$array["isSuccess"] = false;

		}
		else {
			$emailText .= "Phone: {$array["phone"]}\n";
		}

		if ($array["isSuccess"]) {
			// envoi de l'email
			$headers = "From: {$array["firstname"]} {$array["name"]} <{$array["email"]}>\r\nReply-To: {$array["email"]}";
			mail($emailTo, "Un nouveau message de votre Site", $emailText, $headers);
		}

		echo json_encode($array);

	}


	function isEmail($var) {
		return filter_var($var, FILTER_VALIDATE_EMAIL);
	}


	function isPhone($var) {
		return preg_match("/^[0-9 ]*$/", $var);
	}


	function verifyInput($var) {
		$var = trim($var);
		$var = stripcslashes($var);
		$var = htmlspecialchars($var);

		return $var;
	}
?>