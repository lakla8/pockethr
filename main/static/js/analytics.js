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


const ctx = document.getElementById("Chart");

const data = {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
        {
            label: "Dataset 1",
            data: [12, 19, 3, 5, 2, 3],
            borderWidth: 1,
            color: "#fffff",
        },
        {
            label: "Dataset 2",
            data: [70, 159, 53, 55, 52, 53],
            borderWidth: 1,
            color: "#fffff",
        },
    ],
};

const chart = new Chart(ctx, {
    type: "bar",
    data: data,
    options: {
        scales: {
            y: {
                beginAtZero: true,
            },
        },
        legend: {
            labels: {
                // переопределение цвета шрифта
                fontColor: "white",
            },
        },
    },
});

$(document).ready(function () {
    // Получаем CSRF-токен из cookie
    const csrftoken = getCookie("csrftoken");

    $("#send_data").click(() => {
        const data = {
            all_in_one: $("#all_in_one").val(),
            networking: $("#networking").val(),
            job_search: $("#job_search").val()
        };
        // Преобразуем объект JSON в строку
        const jsonData = JSON.stringify(data);
        $.ajax({
            url: `/analytics/save_data/`,
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
