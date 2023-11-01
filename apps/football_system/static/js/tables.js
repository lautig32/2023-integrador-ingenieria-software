function searchTable() {
    var input, filter, table, tr, th, td, i, j;
    input = document.getElementById("matches-search");
    filter = input.value.toUpperCase();
    table = document.getElementById("matches-tbl");
    tr = table.getElementsByTagName("tr");
    
    th = tr[0].getElementsByTagName("th");
    for (i = 0; i < th.length; i++) {
        th[i].style.display = "";
    }
    
    for (i = 1; i < tr.length; i++) {
        td = tr[i].getElementsByTagName("td");
        var found = false;  
        
        for (j = 0; j < td.length; j++) {
            if (td[j].innerHTML.toUpperCase().indexOf(filter) > -1) {
                found = true; 
                break;  
            }
        }
        
        tr[i].style.display = found ? "" : "none";
    }
}


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
