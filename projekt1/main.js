function openmenu() {
    var menu = document.getElementById("menu");
    menu.style.right = "0";
    menu.hover.after.style.width = "0";

}

function closemenu() {
    menu.style.right = "-200px";
}

function changeTheme() {
    let themeLink = document.getElementById("theme-link");

    console.log(window.sessionStorage.getItem("dark_theme"));

    if (window.sessionStorage.getItem("dark_theme") === "true") {
        themeLink.href = "light.css";
        window.sessionStorage.setItem("dark_theme", "false");
    } else {
        themeLink.href = "style.css";
        window.sessionStorage.setItem("dark_theme", "true");
    }
}