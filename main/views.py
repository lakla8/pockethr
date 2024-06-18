import json
import requests


from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest


def home_view(request):
    """Отображение шаблона домашней страницы."""
    return render(request, "index.html")


def account_view(request):
    """Отображение шаблона страницы аккаунта."""
    with open("main/static/database/database.json", "r+", encoding="utf-8") as file:
        data = json.load(file)
    return render(request, "my_account.html", context=data)


def job_search_view(request):
    """Отображение шаблона страницы поиска вакансий."""
    return render(request, "job_search_view.html")


def job_search(request):
    return render(request, "job_search.html")


def clients_view(request):
    """Отображение шаблона страницы клиентов."""
    return render(request, "clients.html")


def networking_view(request):
    return render(request, "networking.html")


def strategies_view(request):
    """Отображение шаблона страницы стратегий."""
    # url = "http://127.0.0.1:9999/strategy/"
    # response = requests.get(url)
    # print(json.loads(response.text))

    return render(request, "strategies.html")


def trackers_view(request):
    """Отображение шаблона страницы трекеров."""
    return render(request, "trackers.html")


def analytics_view(request):
    """Отображение шаблона страницы аналитики."""
    return render(request, "analytics.html")


def personal_information_view(request):
    """Отображение шаблона страницы с личной информацией."""
    return HttpResponse('Ok')


def client_in_job_search_view(request):
    """Отображение шаблона страницы клиента в поиске работы."""
    return render(request, 'client_in_job_search.html')


def account_info_view(request):
    return render(request, "account_info.html")


def client_in_networking_view(request):
    """Отображение шаблона страницы клиента в нетворкинге."""
    return HttpResponse('Ok')


def goal_view(request):
    """Отображение шаблона страницы целей."""
    return render(request, "goal.html")


def goal_data(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")
    try:
        data = json.loads(request.body.decode("utf-8"))

        print(data)
        return HttpResponse('Ok')
        # url = "http://127.0.0.1:9999/goal/"
        # headers = {
        #     "Content-type": "application/json",
        #     "Accept": "application/json",
        #     "Content-Encoding": "utf-8"
        # }

        # response = requests.post(url,
        #                          data=json.dumps(information), headers=headers
        #                          )
        #
        # print(json.loads(response.text))
    except Exception as e:
        return HttpResponseBadRequest("Ошибка при обработке запроса.")


def analytics_api(request):
    try:
        data = json.loads(request.body.decode("utf-8"))
        return HttpResponse('Ok')
        # url = "http://127.0.0.1:9999/analytics/"

        # headers = {
        #     "Content-type": "application/json",
        #     "Accept": "application/json",
        #     "Content-Encoding": "utf-8"
        # }

        # response = requests.post(url,
        #                          data=json.dumps(information), headers=headers
        #                          )
    except Exception as e:
        return HttpResponseBadRequest("Ошибка при обработке запроса.")


def save_account_info(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    try:
        new_data = json.loads(request.body.decode("utf-8"))

        with open("main/static/database/database.json", "r+", encoding="utf-8") as file:
            data = json.load(file)

        for key in data.keys():
            if new_data[key] != '':
                data[key] = new_data[key]

        with open("main/static/database/database.json", "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

        return HttpResponse('Ok')
    except Exception as e:
        return HttpResponseBadRequest("Ошибка при обработке запроса.")


def in_development(request):
    return render(request, "in_development.html")


def save_job_search(request):
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    try:
        data = json.loads(request.body.decode("utf-8"))
        with open("main/static/database/job_search.json", "w+", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False)

        return HttpResponse('Ok')
    except Exception as e:
        return HttpResponseBadRequest("Ошибка при обработке запроса.")
