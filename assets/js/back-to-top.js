// Back to top button
var width_1 = "";
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
  const switch_1 = document.getElementById("switchlabel_index");
  const abc = switch_1.parentElement.getElementsByTagName('aside')[0];
  if(switch_1){
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
    // switch_1.addEventListener("click", (e) => {
    //   if(abc.style.display === 'block'){
    //     abc.classList.add("opacity-0");
    //     abc.style.transform = "translateX(-100%)";
    //   }
    //   else{
    //     abc.classList.remove("opacity-0");
    //     abc.style.transform = "translateX(0)";
    //   }
    // });
  } 
});

document.addEventListener("DOMContentLoaded", function () {
  const switches = document.querySelectorAll("#switchlabel_toc");
  switches.forEach(function (switch_1) {
    document.addEventListener("scroll", () => {
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
    // switch_1.addEventListener("click", () => {
     
    // });
  });
});

function scrollUp() {
  window.scroll({
    top: 0,
    left: 0,
    behavior: "smooth",
  });
}
