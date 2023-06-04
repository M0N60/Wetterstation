<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daten der Wetterstation der BBST</title>
</head>
<body>
    <?php
    // werte von python ?? how XD
    // maybe wir lassen ne graf machen und exportieren den als img was wir aufrufen könnten

    // werte der HTML
    $Niederschlag =$_REQUEST("Niederschlag"); 
    $Temperatur =$_REQUEST("Temperatur"); 
    $Windstärke =$_REQUEST("Windstärke"); 
    $Windrichtung =$_REQUEST("Windrichtung"); 
    $Luftfeuchtigkeit =$_REQUEST("Luftfeuchtigkeit"); 
    $Luftdruck =$_REQUEST("Luftdruck"); 

    // arry aus den werten von 
    $auswal = array($Niederschlag , $Temperatur, $Windstärke, $Windrichtung, $Luftfeuchtigkeit, $Luftdruck);


    // abfrage des arrays
    if ($auswal[0] == true ) { //erste stelle (Niederschlag) 
        # code... sachen anzeigen für Niederschlag
    }
    else {
        break;
    }
    if ($auswal[1] == true ) { //zweite stelle (Temperatur) 
        # code...sachen anzeigen für Temperatur
    }



    //{}
    ?>
    <a href="main.html">Zurück auf die Startseite</a>   
</body>
</html>