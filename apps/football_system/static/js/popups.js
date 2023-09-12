
let popupPlayer = document.getElementById("popup-upload-player");
function openPopupPlayer(){
    popupPlayer.classList.add("open-popup");
}
function closePopupPlayer(){  
    popupPlayer.classList.remove("open-popup");
}

let popupTeam = document.getElementById("popup-upload-team");
function openPopupTeam(){
    popupTeam.classList.add("open-popup");
}
function closePopupTeam(){
    popupTeam.classList.remove("open-popup");
}

let popupMatch = document.getElementById("popup-upload-match");
function openPopupMatch(){
    popupMatch.classList.add("open-popup");
}
function closePopupMatch(){
    popupMatch.classList.remove("open-popup");
}


function changeFileInputColor(){
    let fileInput = document.getElementsByClassName("file-input");
    for (let i = 0; i < fileInput.length; i++) {
        fileInput[i].classList.add("file-input-txt");
        if(fileInput.classList.contains("file-input-txt")){
            fileInput.classList.add("span");
        }
    }
}

