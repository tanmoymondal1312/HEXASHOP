
function checkFileInput() {
    const saveBtn = document.getElementById("saveBtn");
    const proInput = document.getElementById("user_profile_picture");

    if (proInput.files.length > 0) {
        saveBtn.style.display = "block";
    } else {
        saveBtn.style.display = "none";
    }
}







// console.log(proInput)






