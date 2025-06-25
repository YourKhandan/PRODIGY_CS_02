const dropArea = document.getElementById('drop-area');
const fileInput = document.getElementById('fileElem');
const fileList = document.getElementById('fileList');
const submitBtn = document.getElementById('submitBtn');
let filesToUpload = [];

function updateFileList() {
    fileList.innerHTML = '';
    if (filesToUpload.length === 0) {
        submitBtn.disabled = true;
        return;
    }
    submitBtn.disabled = false;
    filesToUpload.forEach((file, index) => {
        const item = document.createElement('div');
        item.className = "mb-1 small d-flex justify-content-between align-items-center";
        item.innerHTML = `📄 ${file.name} 
            <button class="btn btn-sm btn-danger ms-2" onclick="removeFile(${index})">❌</button>`;
        fileList.appendChild(item);
    });
}

function removeFile(index) {
    filesToUpload.splice(index, 1);
    updateFileList();
}

fileInput.addEventListener('change', (e) => {
    filesToUpload.push(...e.target.files);
    updateFileList();
});

dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.classList.add('border-primary');
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('border-primary');
});

dropArea.addEventListener('drop', (e) => {
    e.preventDefault();
    dropArea.classList.remove('border-primary');
    const droppedFiles = Array.from(e.dataTransfer.files);
    filesToUpload.push(...droppedFiles);
    updateFileList();
});

document.getElementById('upload-form').addEventListener('submit', function (e) {
    const formData = new FormData();
    filesToUpload.forEach(file => formData.append('files', file));
    const xhr = new XMLHttpRequest();
    xhr.open('POST', this.action, true);
    xhr.onload = function () {
        if (xhr.status === 200) {
            window.location.href = xhr.responseURL;
        } else {
            alert('Upload failed!');
        }
    };
    xhr.send(formData);
    e.preventDefault();
});
