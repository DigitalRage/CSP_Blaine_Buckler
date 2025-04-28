let holNRok = [
    "https://southwestcontemporary.com/wp-content/uploads/2023/10/IMG_0426.jpg",
    "https://milliverstravels.com/wp-content/images/Hole-in-the-Rock-arrow.jpg","https://southwestcontemporary.com/wp-content/uploads/2023/10/IMG_0351.jpg"
];
let count = 0;

function change() {
    count += 1; 
    if (count >= holNRok.length) { 
        count = 0;
    }
    document.getElementById("Images").src = holNRok[count]; 
}

setInterval(change, 3000); 
