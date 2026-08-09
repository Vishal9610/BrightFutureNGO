/* =========================
   IMPACT COUNTERS
========================= */

const counters = document.querySelectorAll(".counter");

counters.forEach((counter) => {

    const update = () => {

        const target = +counter.getAttribute("data-target");
        const count = +counter.innerText;

        const speed = 50;
        const increment = Math.ceil(target / speed);

        if (count < target) {

            counter.innerText = count + increment;

            setTimeout(update, 40);

        } else {

            counter.innerText = target;

        }
    };

    update();

});


/* =========================
   TESTIMONIAL SLIDER
========================= */

let slides = document.querySelectorAll(".slide");
let index = 0;

function showSlide() {

    if (slides.length === 0) {
        return;
    }

    slides.forEach((slide) => {
        slide.classList.remove("active");
    });

    index++;

    if (index > slides.length) {
        index = 1;
    }

    slides[index - 1].classList.add("active");
}

if (slides.length > 0) {

    showSlide();

    setInterval(showSlide, 3000);

}


/* =========================
   FAQ ACCORDION
========================= */

const questions = document.querySelectorAll(".faq-question");

questions.forEach((question) => {

    question.addEventListener("click", function () {

        const answer = this.nextElementSibling;

        if (!answer) {
            return;
        }

        if (answer.style.display === "block") {

            answer.style.display = "none";

        } else {

            document.querySelectorAll(".faq-answer").forEach((item) => {
                item.style.display = "none";
            });

            answer.style.display = "block";
        }

    });

});


/* =========================
   GALLERY IMAGE POPUP
========================= */

let images = [];
let currentIndex = 0;
let scale = 1;

document.addEventListener("DOMContentLoaded", function () {

    images = document.querySelectorAll(".gallery-card img");

});


/* Show Current Image */

function showImage() {

    if (images.length === 0) {
        return;
    }

    const popup = document.getElementById("popupImage");
    const caption = document.getElementById("caption");
    const counter = document.getElementById("counter");

    if (!popup) {
        return;
    }

    scale = 1;

    popup.src = images[currentIndex].src;

    popup.style.transform = "scale(1)";

    if (caption) {
        caption.innerHTML = images[currentIndex].alt;
    }

    if (counter) {
        counter.innerHTML =
            (currentIndex + 1) + " / " + images.length;
    }

}


/* Open Image */

function openImage(index) {

    currentIndex = index;

    const modal = document.getElementById("imageModal");

    if (!modal) {
        return;
    }

    modal.style.display = "block";

    showImage();

}


/* Close Image */

function closeImage() {

    const modal = document.getElementById("imageModal");

    if (modal) {
        modal.style.display = "none";
    }

}


/* Next Image */

function nextImage() {

    if (images.length === 0) {
        return;
    }

    currentIndex++;

    if (currentIndex >= images.length) {
        currentIndex = 0;
    }

    showImage();

}


/* Previous Image */

function previousImage() {

    if (images.length === 0) {
        return;
    }

    currentIndex--;

    if (currentIndex < 0) {
        currentIndex = images.length - 1;
    }

    showImage();

}


/* =========================
   IMAGE ZOOM
========================= */

function zoomIn() {

    const popup = document.getElementById("popupImage");

    if (!popup) {
        return;
    }

    scale += 0.2;

    popup.style.transform =
        "scale(" + scale + ")";

}


function zoomOut() {

    const popup = document.getElementById("popupImage");

    if (!popup) {
        return;
    }

    if (scale > 0.4) {
        scale -= 0.2;
    }

    popup.style.transform =
        "scale(" + scale + ")";

}


function resetZoom() {

    const popup = document.getElementById("popupImage");

    if (!popup) {
        return;
    }

    scale = 1;

    popup.style.transform =
        "scale(1)";

}


/* =========================
   KEYBOARD CONTROLS
========================= */

document.addEventListener("keydown", function (e) {

    const modal = document.getElementById("imageModal");

    if (!modal || modal.style.display !== "block") {
        return;
    }

    if (e.key === "ArrowRight") {
        nextImage();
    }

    if (e.key === "ArrowLeft") {
        previousImage();
    }

    if (e.key === "Escape") {
        closeImage();
    }

});


/* =========================
   CLOSE MODAL ON BACKGROUND
========================= */

const modal = document.getElementById("imageModal");

if (modal) {

    modal.addEventListener("click", function (e) {

        if (e.target === this) {
            closeImage();
        }

    });

}