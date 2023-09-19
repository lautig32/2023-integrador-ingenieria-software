
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


let popupMatchData = document.getElementById("popup-match-data");
function openPopupMatchData(){
    popupMatchData.classList.add("open-popup");
}
function closePopupMatchData(){
    popupMatchData.classList.remove("open-popup");
}


function changeFileInputColor(){
    let fileInput = document.getElementsByClassName("file-input");
    let span = document.getElementsByClassName("file-input-spn");
    for (let i = 0; i < fileInput.length; i++) {
        fileInput[i].classList.add("input-txt");
        span.classList.add("span");
    }
}

//mostrar equipo dependiendo de categoria
const matchCategorySelect = document.getElementById('match-category-slct');
const teamOneSelect = document.getElementById('team-one-name');
matchCategorySelect.addEventListener('change', function () {
    const selectedCategory = matchCategorySelect.value;
    const filteredTeams = teams.filter(team => team.category === selectedCategory);
    while (teamOneSelect.options.length > 0) {
        teamOneSelect.remove(0);
    }
    filteredTeams.forEach(team => {
        const option = document.createElement('option');
        option.value = team.id;
        option.text = team.name;
        teamOneSelect.appendChild(option);
    });
});