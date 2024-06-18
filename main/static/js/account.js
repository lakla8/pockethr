// Функция для получения значения cookie по имени
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === name + "=") {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}


$(document).ready(function () {
    // Получаем CSRF-токен из cookie
    const csrftoken = getCookie("csrftoken");

    $("#save_account_info").click(() => {
        const data = {
            position: $("#position").val(),
            role: $("#role").val(),
            interests: $("#interests").val(),
            indusrty: $("#indusrty").val(),
            location: $("#location").val(),
            company: $("#company").val(),
            goals: $("#goals").val()
        };
        // Преобразуем объект JSON в строку
        const jsonData = JSON.stringify(data);
        $.ajax({
            url: `/account/save/`,
            type: "POST",
            headers: {
                "Content-Type": "application/json",
                "X-CSRFToken": csrftoken,
            },
            data: jsonData,
            success: function (response) {
                console.log('OK')
            },
            error: function (error) {
                console.error("Error sending message:", error);
            },
        });
    });
})
