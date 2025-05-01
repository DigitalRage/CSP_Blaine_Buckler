(function() {
    let holNRok = [
        "https://southwestcontemporary.com/wp-content/uploads/2023/10/IMG_0426.jpg",
        "https://milliverstravels.com/wp-content/images/Hole-in-the-Rock-arrow.jpg",
        "https://southwestcontemporary.com/wp-content/uploads/2023/10/IMG_0351.jpg", 
        "https://i.ytimg.com/vi/CLNhlnRh8nQ/maxresdefault.jpg"
    ];

    let fishImages = [
        "https://cdn.allmoab.com/images/content/9805_8870_Green_River_Utah_Fishing_lg.jpg",
        "https://i.ytimg.com/vi/yadME4fOSJg/sddefault.jpg"
    ]; 

    let rokCount = 0;
    let fishCount = 0;

    function rokChange() {
        rokCount = (rokCount + 1) % holNRok.length;
        document.getElementById("rok").src = holNRok[rokCount];
    }
    setInterval(rokChange, 3000);

    function changeFishOnHover() {
        fishCount = (fishCount + 1) % fishImages.length;
        console.log("Fish image changed to:", fishImages[fishCount]); 
        const fishElement = document.getElementById("fsh");
        if (fishElement) {
            fishElement.src = fishImages[fishCount];
        } else {
            console.error("Image element with id 'fsh' not found."); 
        }
    }
    
    document.addEventListener("DOMContentLoaded", function() {
        const fishElement = document.getElementById("fsh");
        if (fishElement) {
            fishElement.addEventListener("mouseover", changeFishOnHover);
            console.log("Hover event listener added."); 
        } else {
            console.error("Image element with id 'fsh' not found."); 
        }
    });
})();

