var slideIndex = 0;
fungsi();

function fungsi() {
    var i;
    var x = document.getElementsByClassName("slideshow", "dot");
    for (i = 0; i < x.length; i++) {
        x[i].style.display = "none";
    }
    slideIndex++;
    if (slideIndex > x.length) { slideIndex = 1 }
    x[slideIndex - 1].style.display = "block";
    setTimeout(fungsi, 5000); // berubah setiap 5 detik
}