// The logic about checkboxes


// When hasChecked changes, we need to update the logic
class WatchedVariable {
    constructor(initialValue) {
      this._value = initialValue;
      this.listeners = new Set();
    }
  
    get value() {
      return this._value;
    }
  
    set value(newValue) {
      const oldValue = this._value;
      this._value = newValue;
      this.listeners.forEach(listener => 
        listener(newValue, oldValue)
      );
    }
  
    onChange(callback) {
      this.listeners.add(callback);
      return () => this.listeners.delete(callback); // returns unsubscribe function
    }
}

// if hasChecked changes, judge the value
let hasChecked = new WatchedVariable(0);
hasChecked.onChange((newValue, oldValue) => {
    const container = document.querySelector(".hoa-filetree-container");
    const links = container.querySelectorAll('a:not(.hoa-filetree-contribute-hint a)');

    Array.from(links).forEach((link) => {
        link.style.display = newValue > 0 ? 'none' : '';
    });

    // console.log(`hasChecked changed from ${oldValue} to ${newValue}`);
});

document.addEventListener("DOMContentLoaded", function () {
    const header = document.querySelector(".hoa-filetree-header");
    const headerInput = header.querySelector("input");

      // check folder
      const folders = document.querySelectorAll(".hoa-filetree-folder");
      Array.from(folders).forEach((folder) => {
        const ul = folder.nextElementSibling;
        const childInputs = ul.querySelectorAll('input');

        // The folder's checkbox
        // TODO: when all children file get checked, then folder will be checked automatically
        const checkbox = folder.querySelector('input');
        checkbox.addEventListener('change', function() {
            if(this.checked) {
                // no check -> checked
                Array.from(childInputs).forEach((childInput) => {

                    // Find whether this element belongs file, If so, hasChecked++
                    const fileParent = childInput.closest('li');

                    // Check if it exists and has the class 'file'
                    if (fileParent && fileParent.classList.contains('hoa-filetree-file')) {
                        if(!childInput.checked) hasChecked.value += 1; // If current file isn't checked, then hasChecked plus one
                        // console.log(hasChecked);
                    }

                    // All elements under the folder get checked
                    childInput.checked = true;
                });

                // Children elements can be seen
                ul.dataset.state = 'open';
                const ulFolders = ul.querySelectorAll('.hoa-filetree-folder');
            
                Array.from(ulFolders).forEach((ulFolder) => {
                    // The child folder become open
                    // If child folder is closed, the open it
                    if(ulFolder.nextElementSibling.dataset.state === 'closed') ulFolder.click();
                });

                // This folder icon need to update
                // no check and close -> checked and open
                // no check and open -> checked and open
                const images = folder.querySelectorAll(".hoa-image-state");
                Array.from(images).forEach((el) => {
                    el.dataset.state = 'open';
                });
            }
            else {
                // checked -> no check
                Array.from(childInputs).forEach((childInput) => {

                    // Find whether this element belongs file, If so, hasChecked--
                    const fileParent = childInput.closest('li');
                    // Check if it exists and has the class 'file'
                    if (fileParent && fileParent.classList.contains('hoa-filetree-file')) {
                        if(childInput.checked) hasChecked.value -= 1; // If current file is checked, then hasChecked minus one
                    }

                    // All elements under the folder out of checked
                    childInput.checked = false;

                });

                // Children elements can't be seen
                ul.dataset.state = 'closed';
                const ulFolders = ul.querySelectorAll('.hoa-filetree-folder');

                Array.from(ulFolders).forEach((ulFolder) => {
                    // The child folder become closed
                    // If child folder is open, then close it
                    if(ulFolder.nextElementSibling.dataset.state === 'open') ulFolder.click();
                });

                // This folder icon need to update
                // checked and close -> no check and close
                // checked and open -> no check and close
                const images = folder.querySelectorAll(".hoa-image-state");
                Array.from(images).forEach((el) => {
                    el.dataset.state = 'closed';
                });
            }
        });

      });

    //  check file
    const files = document.querySelectorAll(".hoa-filetree-file");
    Array.from(files).forEach((file) => {

        // If at least one file get checked, then display:none
        const checkbox = file.querySelector('input');
        checkbox.addEventListener('change', function() {
            if(this.checked) {
                // no check -> checked
                hasChecked.value += 1;

                const ulParent = file.closest('ul');
                const folderParent = ulParent.previousElementSibling;
                
                
                // judge all the sibling element(ulParent's children)
                let allChecked = true;
                Array.from(ulParent.children).forEach((el) => {
                    const childInput = el.querySelector('input');
                    if(!childInput.checked) allChecked = false;
                })
                // all file are checked
                if(allChecked){
                    // parent -> folder
                    if(folderParent && folderParent.classList.contains('hoa-filetree-folder')) {
                        const folderParentInput = folderParent.querySelector('input');
                        folderParentInput.checked = true;
                    }
                    // parent -> container
                    if(folderParent && !folderParent.classList.contains('hoa-filetree-folder')) {
                        headerInput.checked = true;
                    }
                }
                
            }
            else {
                // checked -> no check
                hasChecked.value -= 1;
                
                const ulParent = file.closest('ul');
                const folderParent = ulParent.previousElementSibling;

                // directly update header to unchecked
                headerInput.checked = false;

                // parent -> folder
                // directly update parent folder to unchecked
                if(folderParent && folderParent.classList.contains('hoa-filetree-folder')){
                    const folderParentInput = folderParent.querySelector('input');
                    folderParentInput.checked = false;
                }
                
            }
        });
    });

    // check header
    headerInput.addEventListener('change', function() {
        if(this.checked) {
            // no check -> checked

            // All files get checked
            Array.from(files).forEach((file) => {
                const checkbox = file.querySelector('input');
                checkbox.checked = true;
                hasChecked.value += 1;
            })
            // All folders get checked
            Array.from(folders).forEach((folder) => {
                const checkbox = folder.querySelector('input');
                checkbox.checked = true;
            })

        } else {
            // checked -> no check

            // All files cancel checked
            Array.from(files).forEach((file) => {
                const checkbox = file.querySelector('input');
                checkbox.checked = false;
                hasChecked.value -= 1;
            })
            // All folders cancel checked
            Array.from(folders).forEach((folder) => {
                const checkbox = folder.querySelector('input');
                checkbox.checked = false;
            })
        }
    })

    // checkbox with shift key holding
    const checkboxes = document.querySelectorAll(".hoa-filetree-container input");
    let lastChecked;
  
    function getChecked(e) {
        // when one checkbox get clicked
        let isBetween = false;
        checkboxes.forEach(checkbox => {
            // if shift key is activated
            if (e.shiftKey) {
            // from this to lastChecked, these checkboxes have isBetween tag
            if (checkbox === this || checkbox === lastChecked) isBetween = !isBetween;

            if (isBetween) {
                // parent -> folder

                //parent -> file
                const liParent = checkbox.closest('li');
                if(liParent.classList.contains('hoa-filetree-file')){

                    if(checkbox !== lastChecked && !checkbox.checked) hasChecked.value += 1;
                    if(checkbox !== lastChecked && checkbox.checked) hasChecked.value -= 1;
                }
                // console.log(lastChecked);

                // according to this checkbox's checked condition
                // last checked & this checked -> between not check
                if(lastChecked.checked && !this.checked) {
                    checkbox.checked = false;
                }
                // last checked & this not checked -> between checked
                else if(lastChecked.checked && this.checked) {
                    checkbox.checked = true;
                } 
                // last not check & this checked -> between not checked
                else if(!lastChecked.checked && !this.checked) {
                    checkbox.checked = false;
                }
                // last not check & this not check -> between checked
                else if(!lastChecked.checked && this.checked) {
                    checkbox.checked = true;
                }
                
            }
            }
        });
        lastChecked = this;
    }
  
    checkboxes.forEach(checkbox => checkbox.addEventListener("click", getChecked));

});




