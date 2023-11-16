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

document.addEventListener("DOMContentLoaded", function () {
  const switch_1 = document.getElementById("switchlabel");
  if (switch_1) {
    document.addEventListener("scroll", (e) => {
      if (window.scrollY > document.scrollingElement.scrollHeight-document.scrollingElement.clientHeight-200) {
        // switch_1.classList.add("opacity-0");
        // switch_1.style.visibility = 'hidden';
        switch_1.style.display = 'none';
      } else {
        // switch_1.classList.remove("opacity-0");
        // switch_1.style.visibility = 'visible';
        switch_1.style.display = 'block';
      }
    });
  }
});

function scrollUp() {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
}
