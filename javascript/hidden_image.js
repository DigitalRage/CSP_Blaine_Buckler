const hiddenArea = document.getElementById("hidden-area");
const hiddenImage = document.getElementById("hidden-image");

hiddenArea.addEventListener("mouseenter", () => {
    hiddenImage.style.display = "block";
});

hiddenArea.addEventListener("mouseleave", () => {
    hiddenImage.style.display = "none";
});
