// Back to top button

document.addEventListener("DOMContentLoaded", function () {
  const backToTop = document.querySelectorAll("#backToTop");
  backToTop.forEach(function (btt) {
    document.addEventListener("scroll", function (e) {
      if (window.scrollY > 300) {
        btt.classList.remove("opacity-0");
      } else {
        btt.classList.add("opacity-0");
      }
    });
  });
});

function scrollUp() {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
}
