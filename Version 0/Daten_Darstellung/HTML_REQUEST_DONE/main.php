<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daten der Wetterstation der BBST</title>
</head>
<body>
    <h1>Hier sind die von Ihnen ausgewählten Daten</h1> 
    <?php
    // werte von python ?? how XD
    // maybe wir lassen ne graf machen und exportieren den als img was wir aufrufen könnten
    // werte der HTML
    $Niederschlag =$_REQUEST["Niederschlag"]; 
    $Temperatur =$_REQUEST["Temperatur"]; 
    $Windstärke =$_REQUEST["Windstärke"]; 
    $Windrichtung =$_REQUEST["Windrichtung"]; 
    $Luftfeuchtigkeit =$_REQUEST["Luftfeuchtigkeit"]; 
    $Luftdruck =$_REQUEST["Luftdruck"]; 

    
    echo"$Niederschlag <br>";
    echo"$Temperatur <br>";
    echo"$Windstärke <br>";
    echo"$Windrichtung <br>";
    echo"$Luftfeuchtigkeit <br>";
    echo"$Luftdruck <br>";

    if ($Niederschlag=="1") { // frage ob niederschlag value 1 ist
        echo "zeige Niederschlag";
    }
    else {
        echo "zeige kein Niederschlag";
    }
    echo"<br>";
    if ($Temperatur=="1") {
        echo "zeige Temperatur";
    }
    else {
        echo "zeige keine Temperatur";
    }
    echo"<br>";
    if ($Windstärke=="1") {
        echo "zeige Windstärke";
    }
    else {
        echo "zeige keine Windstärke";
    }
    echo"<br>";
    if ($Windstärke=="1") {
        echo "zeige Windrichtung";
    }
    else {
        echo "zeige keine Windrichtung";
    }
    echo"<br>";
    if ($Luftfeuchtigkeit=="1") {
        echo "zeige Luftfeuchtigkeit";
    }
    else {
        echo "zeige keine Luftfeuchtigkeit";
    }
    echo"<br>";
    if ($Luftdruck=="1") {
        echo "zeige Luftdruck";
    }
    else {
        echo "zeige kein Luftdruck";
    }
    echo"<br>";
    ?>  
    <a href="main.html">Zurück auf die Startseite</a>  
</body>
</html>