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


