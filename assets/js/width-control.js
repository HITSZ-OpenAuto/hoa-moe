document.addEventListener('DOMContentLoaded', function(){
    const switchButton = document.querySelector(".hoa-width-button");
    const pages = document.querySelector('.hoa-page');

    if (!switchButton && pages) {
        pages.dataset.size = "xl";
        return;
    }

    if (switchButton && pages) {
        if(!sessionStorage.getItem("page-width")){
            sessionStorage.setItem("page-width", "xl");
        }

        const switchWidth = () => {
            if(sessionStorage.getItem("page-width") === "2xl"){
                sessionStorage.setItem("page-width", "xl");
            } else if(sessionStorage.getItem("page-width") === "xl") {
                sessionStorage.setItem("page-width", "2xl");
            } else {
                throw new Error("Invalid page width");
            }
        }
        
        console.log(sessionStorage.getItem("page-width"));
        pages.dataset.size = sessionStorage.getItem("page-width");

        switchButton.addEventListener("click", ()=>{
            try {
                switchWidth();
                console.log(sessionStorage.getItem("page-width"));
                pages.dataset.size = sessionStorage.getItem("page-width");
                console.log(pages.dataset.size);
            } catch (error) {
                console.log(`${error}`);
            }
        });
    }
});