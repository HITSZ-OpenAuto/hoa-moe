// download checked file

function downloadFile(url, index) {
    const iframe = document.createElement('iframe');
    iframe.style.display = 'none';
    iframe.src = url;
    iframe.id = 'download_iframe_' + index;
    // a.download = fileName;
    document.body.appendChild(iframe);
    // a.click();

}

document.addEventListener("DOMContentLoaded", function() {
    const downloadButton = document.querySelector('.hoa-filetree-download');
    downloadButton.addEventListener('click', () => {
        // get all checked file
        let links = [];
        const files = document.querySelectorAll('.hoa-filetree-file');
        Array.from(files).forEach((file, index) => {
            const checkbox = file.querySelector('input');
            if(checkbox.checked){
                const link = file.querySelector('.hoa-filetree-download-link');
                links.push(link);
                downloadFile(link.href);
            }
        });
        setTimeout(() => {
            links.forEach((url, index) => {
                let iframe = document.getElementById('download_iframe_' + index);
                document.body.removeChild(iframe);
            });
        }, 3000);
    });
});