// Função para salvar a preferência de cor no localStorage e sinalizar atualização
function saveColorPreference(color) {
    localStorage.setItem("colorPreference", color);
    localStorage.setItem("colorPreferenceUpdated", "true"); // Sinaliza atualização
}

document.addEventListener("DOMContentLoaded", function () {
    const colorSwitch = document.getElementById("colorSwitch");
    const body = document.body;

    const savedColorPreference = localStorage.getItem("colorPreference");
    const colorPreferenceUpdated = localStorage.getItem("colorPreferenceUpdated");

    if (savedColorPreference) {
        body.style.backgroundColor = savedColorPreference;
    }

    if (colorPreferenceUpdated === "true") {
        localStorage.setItem("colorPreferenceUpdated", "false");// Marcar como atualizado e redefinir a preferência de cor
        colorSwitch.checked = savedColorPreference === "#1F1F1F";// Atualizar o estado do botão
    }

    colorSwitch.addEventListener("change", function () {
        if (colorSwitch.checked) {
            body.style.backgroundColor = "#000";
            saveColorPreference("#1F1F1F");
        } else {
            body.style.backgroundColor = "#fff";
            saveColorPreference("#fff");
        }
    });

    window.addEventListener("beforeunload", function () {
        const currentBackgroundColor = body.style.backgroundColor;
        saveColorPreference(currentBackgroundColor);
    });
});
