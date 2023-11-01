
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
function openPopupMatchData(matchID){
    popupMatchData.classList.add("open-popup");
    localStorage.setItem('currentMatchID', matchID);
    
    const prueba = document.querySelector('.prueba');
    const currentMatchID = localStorage.getItem('currentMatchID');
    prueba.textContent = currentMatchID;

    console.log(matchID); 
}
function closePopupMatchData(){
    popupMatchData.classList.remove("open-popup");
}

let popupTeamData = document.getElementById("popup-team-data");
function openPopupTeamData(){
    popupTeamData.classList.add("open-popup");
}
function closePopupTeamData(){
    popupTeamData.classList.remove("open-popup");
}

let popupPlayerData = document.getElementById("popup-player-data");
function openPopupPlayerData(){
    popupPlayerData.classList.add("open-popup");
}
function closePopupPlayerData(){
    popupPlayerData.classList.remove("open-popup");
}

function changeFileInputColor(){
    let fileInput = document.getElementsByClassName("file-input");
    let span = document.getElementsByClassName("file-input-spn");
    for (let i = 0; i < fileInput.length; i++) {
        fileInput[i].classList.add("input-txt");
        span.classList.add("span");
    }
}

function enableEdition(){
    let textInput = document.getElementsByClassName("text-input");
    let fileInput = document.getElementsByClassName("file-input");
    textInput.removeAttribute('disabled');
    fileInput.removeAttribute('disabled');
}

//no mostrar equipo local en select de equipo visitante
function updateTeamOptions() {
    var matchCategorySelect = document.getElementById('match-category-slct');
    var teamOneSelect = document.getElementById('team-one-name');
    var teamTwoSelect = document.getElementById('team-two-name');
    
    var selectedCategory = matchCategorySelect.value;
    var filteredTeams = teams.filter(team => team.category === selectedCategory);

    // Limpia las opciones actuales del segundo select
    while (teamTwoSelect.options.length > 0) {
        teamTwoSelect.remove(0);
    }

    // Agrega las nuevas opciones basadas en la categoría seleccionada
    filteredTeams.forEach(team => {
        var option = document.createElement('option');
        option.value = team.id;
        option.text = team.name;
        teamTwoSelect.appendChild(option);
    });
}


