// download checked file

function triggerDownload(blob, fileName) {
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = fileName || "download"; // 设置下载文件名
    document.body.appendChild(a);
    a.click();
    document.body.removeChild(a);
    setTimeout(() => URL.revokeObjectURL(url), 5000);
}

async function downloadFile(url, setProgress) {
    const response = await fetch(url);
    if (!response.ok) {
        throw new Error(`HTTP ERROR! CODE: ${response.status}`);
    }
    const contentLength = response.headers.get("Content-Length");
    const total = parseInt(contentLength) || null;
    let loaded = 0;

    const reader = response.body.getReader();
    const chunks = [];

    while (true) {
        const {done, value} = await reader.read();
        if (done) break;
        chunks.push(value);
        loaded += value.length;

        setProgress(total ? (loaded / total * 100) : 99);
    }
    setProgress(100);
    const blob = new Blob(chunks);
    triggerDownload(blob, decodeURIComponent(url.split('/').pop()));
}

document.addEventListener("DOMContentLoaded", function () {
    const downloadButton = document.querySelector('.hoa-filetree-download');
    downloadButton.addEventListener('click', () => {
        // get all checked file
        const files = document.querySelectorAll('.hoa-filetree-file');
        Array.from(files).forEach((file) => {
            const checkbox = file.querySelector('input');
            if (checkbox.checked) {
                const link = file.querySelector('.hoa-filetree-download-link');
                link.click();
            }
        });
    });

    const downloadFileButtons = document.querySelectorAll('.hoa-filetree-download-link');
    downloadFileButtons.forEach(ele => ele.addEventListener('click', (e) => {
        e.stopPropagation();
        e.preventDefault();
        // get link
        const url = e.target.dataset.url;
        // hide icon and show progress
        e.target.style.display = 'none';
        const progressWrapper = e.target.parentElement.querySelector(".hoa-filetree-download-progress-wrap");
        progressWrapper.style.display = `block`;
        const progressCircle = progressWrapper.querySelector(".hoa-filetree-download-progress");
        const progressText = progressWrapper.querySelector(".hoa-filetree-download-progress-text");
        const setProgress = (progress) => {
            // console.log(progress)
            const deg = progress * 3.6;
            progressCircle.style.background = `conic-gradient(#1677ff 0, #1677ff ${deg}deg, transparent ${deg}deg, transparent 360deg)`;
            progressText.innerText = progress.toFixed(0);
        }
        setProgress(0);
        downloadFile(url, setProgress).then(() => {
            e.target.style.display = '';
            progressWrapper.style.display = ``;
        }).catch();
        console.log(url);
    }));

    /* preview
    const previewFileButtons = document.querySelectorAll('.hoa-filetree-preview-link');
    previewFileButtons.forEach(ele => ele.addEventListener('click', (e) => {
        e.stopPropagation();
        e.preventDefault();
        // get link
        const url = e.target.dataset.url;
        const iframe = document.createElement('iframe');
        iframe.style.position = "fixed";
        iframe.style.height = "100vh";
        iframe.style.width = "100vw";
        iframe.style.left = "0";
        iframe.style.top = "0";
        iframe.style.zIndex = "9999";
        iframe.src = url;
        iframe.id = 'preview_iframe';
        document.body.appendChild(iframe);
    }));
    */
});