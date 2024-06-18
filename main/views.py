import json
import requests


from django.shortcuts import render, HttpResponse
from django.http import HttpResponseBadRequest


def home_view(request):
    """Отображение шаблона домашней страницы."""
    return render(request, "index.html")


def account_view(request):
    """Отображение шаблона страницы аккаунта."""
    return HttpResponse('Ok')


def job_search_view(request):
    """Отображение шаблона страницы поиска вакансий."""
    return render(request, "job_search_view.html")


def job_search(request):
    return render(request, "job_search.html")


def clients_view(request):
    """Отображение шаблона страницы клиентов."""
    return render(request, "clients.html")


def networking_view(request):
    return HttpResponse('Ok')


def strategies_view(request):
    """Отображение шаблона страницы стратегий."""
    return render(request, "strategies.html")


def trackers_view(request):
    """Отображение шаблона страницы трекеров."""
    return HttpResponse('Ok')


def analytics_view(request):
    """Отображение шаблона страницы аналитики."""
    return render(request, "analytics.html")


def personal_information_view(request):
    """Отображение шаблона страницы с личной информацией."""
    return HttpResponse('Ok')


def client_in_job_search_view(request):
    """Отображение шаблона страницы клиента в поиске работы."""
    return render(request, 'client_in_job_search.html')


def client_in_networking_view(request):
    """Отображение шаблона страницы клиента в нетворкинге."""
    return HttpResponse('Ok')


def goal_view(request):
    """Отображение шаблона страницы целей."""
    return HttpResponse('Ok')

def analytics_api(request):
    """Обращение в API, которая возвращает список рекомендованных мест."""
    if request.method != "POST":
        return HttpResponseBadRequest("Invalid request method.")

    try:
        data = json.loads(request.body.decode("utf-8"))
        print(data)
        return HttpResponse('Ok')
        # features = [item for item in data["features"]
        #             if data["features"][item] == "1"]

        # users_recommendations = [
        #     [item["id"] for item in UserProfile.objects.get(user=user).recommendations if item["is_selected"] == "1"]
        #     for user in meet.users.all()
        # ]

        # information = {
        #     "features": features,
        #     "users_recommendations": users_recommendations
        # }

        # url = "http://127.0.0.1:9999/algorithm?id_const=true"
        # headers = {
        #     "Content-type": "application/json",
        #     "Accept": "application/json",
        #     "Content-Encoding": "utf-8"
        # }

        # response = requests.post(url,
        #                          data=json.dumps(information), headers=headers
        #                          )

        # place_id = [item[0] for item in json.loads(response.text)['result']]
        # places_object = [Place.objects.filter(location_id=value)[0] for value in place_id]
        # place = [{
        #     "path_image": place.path_image,
        #     "id": place.id,
        #     "name": place.name,
        #     "rating": float(place.rating)
        # } for place in places_object]

        # meet.recommendations = place
        # meet.save(update_fields=["recommendations"])

        # return JsonResponse({"meet_id": meet_id})
    except Exception as e:
        return HttpResponseBadRequest("Ошибка при обработке запроса.")