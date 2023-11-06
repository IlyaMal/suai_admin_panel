var checkbox = document.getElementById("disableInput");
var textInput = document.getElementById("textInput");

    // Обработчик изменения состояния чекбокса
checkbox.addEventListener("change", function() {
    if (checkbox.checked) {
        textInput.disabled = true; // Блокируем текстовое поле
    } else {
        textInput.disabled = false; // Разблокируем текстовое поле
    }
});