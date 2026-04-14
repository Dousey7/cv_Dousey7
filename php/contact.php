<?php
require '../PHPMailer-master/src/Exception.php';
require '../PHPMailer-master/src/PHPMailer.php';
require '../PHPMailer-master/src/SMTP.php';

use PHPMailer\PHPMailer\PHPMailer;
use PHPMailer\PHPMailer\Exception;

// Configuration SMTP Gmail (vos identifiants)
$smtpHost = 'smtp.gmail.com';
$smtpUsername = 'seydaw7@gmail.com';     // ⚠️ Remplacez par votre Gmail
$smtpPassword = 'hgwy hyuv cuvh unte'; // ⚠️ Le mot de passe d'application
$smtpPort = 587;
$smtpSecure = 'tls';

$emailTo = "seydaw7@gmail.com"; // L'adresse qui recevra les messages

$array = array(
    'firstname' => '', 'name' => '', 'email' => '', 'phone' => '', 'message' => '',
    'firstnameError' => '', 'nameError' => '', 'emailError' => '', 'phoneError' => '', 'messageError' => '',
    'isSuccess' => false
);

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $array["firstname"] = verifyInput($_POST["firstname"]);
    $array["name"] = verifyInput($_POST["name"]);
    $array["email"] = verifyInput($_POST["email"]);
    $array["phone"] = verifyInput($_POST["phone"]);
    $array["message"] = verifyInput($_POST["message"]);
    $array["isSuccess"] = true;
    $emailText = "";

    // Validations
    if (empty($array["firstname"])) {
        $array["firstnameError"] = "Je veux connaitre ton prénom !";
        $array["isSuccess"] = false;
    } else {
        $emailText .= "FirstName: {$array["firstname"]}\n";
    }

    if (empty($array["name"])) {
        $array["nameError"] = "Et oui je veux tout savoir. Meme ton nom !";
        $array["isSuccess"] = false;
    } else {
        $emailText .= "Name: {$array["name"]}\n";
    }

    if (empty($array["message"])) {
        $array["messageError"] = "Que voulez-vous me dire S'il vous plait ?!";
        $array["isSuccess"] = false;
    } else {
        $emailText .= "Message: {$array["message"]}\n";
    }

    if (!isEmail($array["email"])) {
        $array["emailError"] = "T'essaies de me rouler ? C'est pas un email ca !";
        $array["isSuccess"] = false;
    } else {
        $emailText .= "Email: {$array["email"]}\n";
    }

    if (!isPhone($array["phone"])) {
        $array["phoneError"] = "Que des chiffres et des espaces ...";
        $array["isSuccess"] = false;
    } else {
        $emailText .= "Phone: {$array["phone"]}\n";
    }

    // Envoi de l'email si tout est valide
    if ($array["isSuccess"]) {
        $mail = new PHPMailer(true);
        try {
            $mail->isSMTP();
            $mail->Host       = $smtpHost;
            $mail->SMTPAuth   = true;
            $mail->Username   = $smtpUsername;
            $mail->Password   = $smtpPassword;
            $mail->SMTPSecure = $smtpSecure;
            $mail->Port       = $smtpPort;

            $mail->setFrom($array["email"], $array["firstname"] . " " . $array["name"]);
            $mail->addReplyTo($array["email"], $array["firstname"] . " " . $array["name"]);
            $mail->addAddress($emailTo, "Destinataire");

            $mail->Subject = "Un nouveau message de votre Site";
            $mail->Body    = $emailText;

            $mail->send();
        } catch (Exception $e) {
            // En cas d'erreur d'envoi, on peut le logger, mais on garde isSuccess = true pour l'utilisateur ?
            // Pour l'utilisateur, on peut afficher une erreur technique.
            $array["isSuccess"] = false;
            $array["messageError"] = "Erreur technique, veuillez réessayer plus tard.";
        }
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