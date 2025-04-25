const hoverImage = document.getElementById("hover-image");
const images = [
    "https://www.rollingstone.com/wp-content/uploads/2025/01/Switch.jpg?w=1581&h=1054&crop=1",
    "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlKekhuSH-iVZy3k-VaNAM1rDuCOWAN8VU1g&s" 
];

hoverImage.onmouseover = function () {
    document.getElementById("hover-image").src = images[1];
};

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

