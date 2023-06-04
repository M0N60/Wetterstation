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
    // maybe wir lassen ne graf machen und exportieren den als img was wir aufrufen könnten


    // dritte idee mit allen in einem namen (array) und dann mit if else

    // (0 = angeklickt, 1 = nicht angeklickt)
    $auswahl = array(1 ,2 ,3 ,4 ,5 ,6);  //aber alles 0 setzen fürt glaube ich zum Problem (die Nachicht )     
    // $auswal = array($Niederschlag , $Temperatur, $Windstärke, $Windrichtung, $Luftfeuchtigkeit, $Luftdruck);
    $auswahl=$_REQUEST["auswahl"]; //array mit den auswahlstatusen 
    
    if ($auswahl[0]==0) {//erste stelle (Niederschlag) 
        echo "aus";
    } 
    else {
        echo "an";
    }

    if ($auswahl[1]==0) {
        echo "aus";
    }
    else {
        echo "an";
    }
    if ($auswahl[2]==0) {
        echo "aus";
    }
    else {
        echo "an";
    }

    /*
    zweite idee mit einzelen Namen (Geht auch aber nervige meldungen wenn nicht angeklickt) 
    und dann mit if else und der REQUEST abfrage der Checkboxen

    if ($_REQUEST["Niederschlag"]==true){
        echo "nds";
    }
    else {
        echo "no nds";
    }

    if ($_REQUEST["Temperatur"]==true){
        echo "temp";
    }
    else {
        echo "no temp";
    }
    */


    /*
    erste idee mit einzelen Namen (selbe wie bei zweiten idee aber ist umstentlicher zu schreiben)

    $Niederschlag=false;
    $Niederschlag=$_REQUEST["Niederschlag"];
    if ($Niederschlag==true) {
        echo "<h1>an</h1>";
    }
    else {
        echo "<h1>aus</h1>";
    }
     */

    ?>
    <a href="main.html">Zurück auf die Startseite</a>   
</body>
</html>