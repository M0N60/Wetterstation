<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Daten</title>
    <link rel="stylesheet" href="Daten.css"></link>
    <script defer src="Daten.js"></script>

</head>
<body>
    <h1 style="text-align: center;">Wir empfelen sich so an zu Ziehen</h1>
    <br><br>
    <?php
        // Variablen
        $Mensch_bild_aktuelle;
        $Regenschirm_an_aus = false;

        // werte aus der Python (sensoren)
        $Temperatur = file_get_contents('/home/praxis/Desktop/txt/Temperatur.txt');
        $Niederschlag = file_get_contents('/home/praxis/Desktop/txt/Niederschlag.txt');
        $Luftdruck = file_get_contents('/home/praxis/Desktop/txt/Luftdruck.txt');
        $Luftfeuchtigkeit = file_get_contents('/home/praxis/Desktop/txt/Luftfeuchtigkeit.txt');
        $Windgeschwindigkeit = file_get_contents('/home/praxis/Desktop/txt/Windgeschwindigkeit.txt');
        $Windrichtung = file_get_contents('/home/praxis/Desktop/txt/Windrichtung.txt');

        // umrachungen für anderer einheiten
        $Luftdruck_psi = $Luftdruck *0.014503773773;
        $Windgeschwindigkeit_kmh = $Windgeschwindigkeit*3.6;

        // Bilder Namen zu variabeln 
        $Mensch_temp0_niederschalg_0 = "menschen/MENSCH1.png";
        $Mensch_temp0_10_niederschalg_0 = "menschen/MENSCH2.png";
        $Mensch_temp10_20_niederschalg_0 = "menschen/MENSCH3.png";
        $Mensch_temp20niederschalg_0 = "menschen/MENSCH4.png";

        $Mensch_temp0_10_niederschalg_1 = "menschen/MENSCH.png";
        $Mensch_temp10_20_niederschalg_1 = "menschen/MENSCH.png";
        $Mensch_temp20niederschalg_1 = "menschen/MENSCH.png";
        

        // Regneschirm  an aus bestimmen 
        if ($Niederschlag >=  3 ) { // in ml/mm²pro stunde
            $Regenschirm_an_aus = true;
        }
        if ( $Temperatur <=  0) {
            $Regenschirm_an_aus = false;
        }

        
        // aufgrund von den Werten das auktuelle Bild aussuchen
        if ( $Regenschirm_an_aus == false) {
            if ($Temperatur <=  0) {
                $Mensch_bild_aktuelle = $Mensch_temp0_niederschalg_0;
            }
            elseif ($Temperatur <=  10) {
                $Mensch_bild_aktuelle = $Mensch_temp0_10_niederschalg_0;
            }
            elseif ($Temperatur <=  20) {
                $Mensch_bild_aktuelle = $Mensch_temp10_20_niederschalg_0;
            }
            else {
                $Mensch_bild_aktuelle = $Mensch_temp20niederschalg_0;
            }
        }
        else {
            if ($Temperatur <=  10) {
                $Mensch_bild_aktuelle = $Mensch_temp0_10_niederschalg_1;
            }
            elseif ($Temperatur <=  20) {
                $Mensch_bild_aktuelle = $Mensch_temp10_20_niederschalg_1;
            }
            else {
                $Mensch_bild_aktuelle = $Mensch_temp20niederschalg_1;
            }
        }
        
        // Ausgabe (vom Bild)
        if ($Regenschirm_an_aus == true){
            echo '<img src="menschen/Regenschirm.png" style="position: absolute; top: 145px; left: 238px; z-index: 155;" alt="Wo Regenschirm">';
        }
    ?>

    <main>
        <?php echo '<img src="'.$Mensch_bild_aktuelle.'" alt="" width="300px" height="400px"'; ?>
        <img id="anchor" src="" alt="" width="200px" height="400px">    <!-- der ancor kann nicht in er php sein deswegen zeigen wir hier auf nichts !!-->
        <div id="eyes">                                                 <!-- einzelen augen mit ihrer classe und (absoluten) position -->
            <img class="eye" src="menschen/EYE.png" style="top: -155px; right: 7px;" width="15px" >
            <img class="eye" src="menschen/EYE.png" style="top: -155px; left: 9px;" width="15px" >
        </div>
    </main>

    <!-- hier sollen einmal die Aktuellen Werte hin ? -->

    <section class="hidden bubble_rot">
        <h2>Die aktuelle <br> Temperatur ist: </h2>
        <p> <?php echo "$Temperatur"; ?> °C </p> 
             
    </section>

    <section class="hidden blue">
        <h2>Der Niederschlags pro Stunde ist:</h2>
        <p> <?php echo "$Niederschlag"; ?> l/m²</p>
        <div class="curve_blau"></div>
    </section>

    <section class="hidden ">
        <h2> Die aktuelle Windrichtung ist</h2>
        <p> <?php echo "$Windrichtung"; ?></p>

    </section>

    <section class="hidden bubble_schwartz">
        <h2> Die aktuelle <br>Windgeschwindigkeit ist</h2>
        <p> <?php echo "$Windgeschwindigkeit"; ?> m/s 
        <br> <?php echo "$Windgeschwindigkeit_kmh"; ?> km/h </p>
        
        
    </section>

    <section class="hidden white">
        <h2> Der aktuelle Luftdruck ist</h2>
        <p> <?php echo "$Luftdruck"; ?> hPa 
        <br> <?php echo "$Luftdruck_psi";?> psi </p>
    </section>

    <section class="hidden pink">
        <h2> Die aktuelle Luftfeuchtigkeit  ist</h2>
        <p> <?php echo "$Luftfeuchtigkeit"; ?> % </p>
        <div class="curve_pink"></div>
    </section>


    <!-- hier sollen die Diagramme hin ? -->

    <section class="hidden">
        <h3> Der verlauf an Hand von <br> Diagrammen:</h3>

        <div class="bilder">
        <div class="bild hidden">
                <img src="diagramm/Temperatur.png" alt="Temperatur" width="250px" height="250px">  
            </div>
            <div class="bild hidden">
                <img src="diagramm/Niederschlag.png" alt="Niederschlag" width="250px" height="250px">  
            </div>
            <div class="bild hidden">
                <img src="diagramm/Luftfeuchtigkeit.png" alt="Luftfeuchtigkeit" width="250px" height="250px">  
            </div>
            <div class="bild hidden">
                <img src="diagramm/Luftdruck.png" alt="Luftdruck" width="250px" height="250px">  
            </div>
        </div>
    </section>
    
</body>
</html>