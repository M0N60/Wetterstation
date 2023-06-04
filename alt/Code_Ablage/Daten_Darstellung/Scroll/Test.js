// um zu sehen welche Browser  https://caniuse.com/?search=IntersectionObserver

const observer = new IntersectionObserver((entries) => {    // startet wenn eon objekt sichtbar wird 
    entries.forEach((entry) => {
        console.log(entry);
        
        if (entry.isIntersecting) {                         // wenn es sichtbar ist wird show class hinzugefägt wenn nicht wieder enfernt 
            entry.target.classList.add('show');
        }
        else {
            entry.target.classList.remove('show');
        }
    });
});

const hiddenElements = document.querySelectorAll('.hidden');// Get all the hidden elements aus Html
hiddenElements.forEach((el) => observer.observe(el));       //überwacht alle hidden elements