function toggleButton(button) {

    if (button.textContent == 'False') {
        button.classList.remove('netral');
        button.classList.remove('off');
        button.classList.add('on');
        button.textContent = 'True';
        button.value='True';
    } else {
        button.classList.remove('netral');
        button.classList.remove('on');
        button.classList.add('off');
        button.textContent = 'False';
        button.value='False';
    }
}

function typeButton(button){

    if (button.textContent == 'False') {
        return 'toggle-btn off';
    } else {
        return 'toggle-btn on';
    }
}

function updateRangeValue(fieldId,value) {
    document.getElementById(fieldId).textContent = value;
}

function increaseValue(fieldId, maxValue) {
    var value = parseInt(document.getElementById(fieldId).value, 10);
    value = isNaN(value) ? 0 : value;
    if (value < maxValue) { // Verifica se o valor é menor que o máximo permitido
        value++;
        document.getElementById(fieldId).value = value;
    }
}

function decreaseValue(fieldId, minValue) {
    var value = parseInt(document.getElementById(fieldId).value, 10);
    value = isNaN(value) ? 0 : value;
    if (value > minValue) { // Verifica se o valor é maior que o mínimo permitido
        value--;
        document.getElementById(fieldId).value = value;
    }
}

function togglePasswordVisibility(fieldId) {
    var passwordInput = document.getElementById(fieldId);
    if (passwordInput.type === 'password') {
        passwordInput.type = 'text';
    } else {
        passwordInput.type = 'password';
    }
}