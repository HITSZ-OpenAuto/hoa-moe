(function() {
    const storedWidth = sessionStorage.getItem("page-width") || "xl";
    document.documentElement.dataset.initialWidth = storedWidth;
    document.documentElement.style.setProperty(
        '--initial-page-width', 
        storedWidth === "xl" ? "1280px" : "1536px"
    );
})();

document.addEventListener('DOMContentLoaded', function(){
    const switchButton = document.querySelector(".hoa-width-button");
    const pages = document.querySelector('.hoa-page');

    if (!switchButton || !pages) return;

    if(!sessionStorage.getItem("page-width")){
        sessionStorage.setItem("page-width", "xl");
    }

    const switchWidth = () => {
        let currentWidth = sessionStorage.getItem("page-width");
        if (currentWidth !== "xl" && currentWidth !== "2xl") {
            currentWidth = "xl";
        }
        const newWidth = currentWidth === "2xl" ? "xl" : "2xl";
        sessionStorage.setItem("page-width", newWidth);
        document.documentElement.style.setProperty(
            '--initial-page-width', 
            newWidth === "xl" ? "1280px" : "1536px"
        );
        pages.dataset.size = newWidth;
    }

    pages.dataset.size = sessionStorage.getItem("page-width");

    switchButton.addEventListener("click", () => {
        try {
            switchWidth();
        } catch (error) {
            console.error(`Failed to switch width: ${error}`);
        }
    });
});