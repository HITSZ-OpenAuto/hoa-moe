// Script for filetree shortcode collapsing/expanding folders used in the theme
// ======================================================================
document.addEventListener("DOMContentLoaded", function () {
    const folders = document.querySelectorAll(".hoa-filetree-folder");
    folders.forEach(function (folder) {
      folder.addEventListener("click", function () {
        let level = 0;
        Array.from(folder.children).forEach(function (el) {
          el.dataset.state = el.dataset.state === "open" ? "closed" : "open";
        });

        // folder icon logic
        const checkbox = folder.querySelector('input');
        const images = folder.querySelectorAll(".hoa-image-state");
        Array.from(images).forEach((el) => {
          let state = el.dataset.state;
          // no check and close -> no check and open
          if(!checkbox.checked && state === 'closed') el.dataset.state = "open";
          // no check and open -> no check and close
          else if(!checkbox.checked && state === 'open') el.dataset.state = "closed";
          // check and close -> check and open
          else if(checkbox.checked && state === 'closed') el.dataset.state = "open";
          // check and open -> check and close
          else if(checkbox.checked && state === 'open') el.dataset.state = "closed";
          
        })

        
        folder.nextElementSibling.dataset.level = `${Math.max(Number(folder.dataset.level) + 1, Number(folder.nextElementSibling.dataset.level))}`;
        level = `${Math.max(Number(folder.nextElementSibling.dataset.level), Number(level))}`;
        
        // add width to placeholder
        Array.from(folder.nextElementSibling.children).forEach((el) => {
          el.dataset.level = `${Math.max(Number(level), Number(el.dataset.level))}`;
          const empty = el.querySelector(".hoa-file-level");
          empty.style.width = `${el.dataset.level * 16}px`;
        })
        
        folder.nextElementSibling.dataset.state = folder.nextElementSibling.dataset.state === "open" ? "closed" : "open";
      });
    });
  });