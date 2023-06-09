<!DOCTYPE html>
<html lang="de">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daten der Wetterstation der BBST</title>
</head>
<body>
    <?php
    // werte von python ?? how XD
    // maybe wir machen eine Graf machen und als img aufrufbar

    // auswahl der HTML
     $Niederschlag =$_REQUEST("Niederschlag"); 
     $Temperatur =$_REQUEST("Temperatur"); 
     $Windstärke =$_REQUEST("Windstärke"); 
     $Windrichtung =$_REQUEST("Windrichtung"); 
     $Luftfeuchtigkeit =$_REQUEST("Luftfeuchtigkeit"); 
     $Luftdruck =$_REQUEST("Luftdruck"); 

    echo"test";
    echo"$Niederschlag";
    echo"<br>";
    // frage ob niederschlag value 1 ist
    if ($Niederschlag=="1") { 
        echo "Es ist Niederschlag";
    }
    else {
        echo "Es ist kein Niederschlag";
    }
    echo"<br>";
    if ($Temperatur=="1") {
        echo "Es ist Temperatur";
    }
    else {
        echo "Es ist keine Temperatur";
    }
    echo"<br>";
    if ($Windstärke=="1") {
        echo "Es ist Windstärke";
    }
    else {
        echo "Es ist keine Windstärke";
    }
    echo"<br>";
    if ($Windstärke=="1") {
        echo "Es ist Windrichtung";
    }
    else {
        echo "Es ist keine Windrichtung";
    }
    echo"<br>";
    if ($Luftfeuchtigkeit=="1") {
        echo "Es ist Luftfeuchtigkeit";
    }
    else {
        echo "Es ist keine Luftfeuchtigkeit";
    }
    echo"<br>";
    if ($Luftdruck=="1") {
        echo "Es ist Luftdruck";
    }
    else {
        echo "Es ist kein Luftdruck";
    }
    echo"<br>";
    ?>
    <!--Link zurück-->
    <a href="main.html">Zurück auf die Startseite</a>   
</body>
</html>