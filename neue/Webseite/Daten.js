// um zu sehen welche Browser scroll-animation unterstützen https://caniuse.com/?search=IntersectionObserver

const observer = new IntersectionObserver((entries) => {    
    entries.forEach((entry) => {
        console.log(entry);    // um zu sehen was passiert 
        
        if (entry.isIntersecting) {                         // wenn es sichtbar ist wird show class hinzugefägt wenn nicht wieder enfernt 
            entry.target.classList.add('show');
        }
        else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden'); // nimmt alle der "hidden" elements aus Html
hiddenElements.forEach((el) => observer.observe(el));       //überwacht alle "hidden" elements

// augen 

const anchor = document.getElementById('anchor')    // id speicher (die vom Objekt)   
const rekt = anchor.getBoundingClientRect();        // position davon ermitteln 
const anchorX = rekt.left + rekt.width / 2;         // x-Koordinate (mitte bilds) speichern
const anchorY = rekt.top + rekt.height / 2;         // y-Koordinate (mitte bilds) speichern
const eye = document.querySelectorAll('.eye')       // nimmt alle der eye-class  


document.addEventListener('mousemove', (e) => {     // gibt die Mausposition aus
    
    const x = e.clientX;                            // x-Koordinate speicher
    const y = e.clientY;                            // y-Koordinate speicher

    const angle = angl(anchorX, anchorY, x, y);     // funktion ausführen (für berechnet des Winkels )
    
    console.log(angle);                             // um zu sehen was passiert 
    
    eye.forEach(eye => {
        eye.style.transform = `rotate(${angle}deg)`; // dreht das eye mit einer "rotate Klasse"
    })
})

function angl(cx, cy, ex, ey) {
    const dy = ey - cy;
    const dx = ex - cx;
    const rad = Math.atan2(dy, dx);                 
    const deg = rad * 180 / Math.PI;                // range (-180, 180) Grad
    return deg;
}