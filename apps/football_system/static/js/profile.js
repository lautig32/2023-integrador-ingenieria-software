document.getElementById('edit-btn').addEventListener('click', function (event) {
    event.preventDefault(); // Prevent form submission or page reload

    let selects = document.getElementsByClassName('select');
    let inputs = document.getElementsByClassName('input');
    let cancelBtn = document.getElementById('cancel-btn');
    let saveBtn = document.getElementById('save-btn');

    for (let i = 0; i < selects.length; i++) {
        selects[i].removeAttribute('disabled');
    }

    for (let i = 0; i < inputs.length; i++) {
        inputs[i].removeAttribute('disabled');
    }

    this.style.display = 'none';
    cancelBtn.style.display = 'inline-block';
    saveBtn.style.display = 'inline-block';
});