const hoverImage = document.getElementById("hover-image");
const images = [
    "https://media.gamestop.com/i/gamestop/20019700/Nintendo-Switch-2", // Original image
    "https://static1.thegamerimages.com/wordpress/wp-content/uploads/wm/2025/04/nintendo-switch-2-camera-peripheral.jpg" // Hover image
];

// Mouseover: Change the image source
hoverImage.onmouseover = function () {
    document.getElementById("hover-image").src = images[1];
};

// Mouseout: Revert the image source
hoverImage.onmouseout = function () {
    document.getElementById("hover-image").src = images[0];
};

function toggleExtraContent() {
    const extraContent = document.getElementById("extra");
    const button = document.getElementById("shw");

    if (extraContent.style.display === "none" || extraContent.style.display === "") {
        extraContent.style.display = "flex";
        button.innerHTML = "Show Less";
    } else {
        extraContent.style.display = "none";
        button.innerHTML = "Show More";
    }
}

