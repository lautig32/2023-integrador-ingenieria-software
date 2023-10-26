function searchTable() {
    var input, filter, table, tr, td, i, j;
    input = document.getElementById("matches-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("matches-tbl");
    tr = table.getElementsByTagName("tr");
    
    for (i = 0; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        var found = false;  // Inicializa la variable found
        
        for (j = 0; j < td.length; j++) {
            if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                found = true;  // Si se encuentra una coincidencia, establece found en true
                break;  // No es necesario buscar más en esta fila
            }
        }
        
        // Muestra u oculta la fila según si se encontró una coincidencia o no
        tr[i].style.display = found ? "" : "none";
    }
};


function filterTable() {
    var select = document.getElementById("table-filter-select");
    var selectedValue = select.value;
    var rows = document.getElementsByClassName("match-row");
    var currentDate = new Date();
    
    for (var i = 1; i < rows.length; i++) {
        var row = rows[i];
        var dateCell = row.querySelector("[data-date]");
        var matchDate = new Date(dateCell.getAttribute("data-date"));
    
        if (selectedValue === "last-matches" && matchDate < currentDate) {
            row.style.display = "table-row";
        } else if (selectedValue === "ongoing-matches" && matchDate >= currentDate) {
            row.style.display = "table-row";
        } else if (selectedValue === "next-matches" && matchDate > currentDate) {
            row.style.display = "table-row";
        } else {
            row.style.display = "none";
        }
    }
}
