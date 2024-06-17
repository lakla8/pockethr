from django.shortcuts import render, HttpResponse


def home_view(request):
    """Отображение шаблона домашней страницы."""
    return render(request, "index.html")


def account_view(request):
    """Отображение шаблона страницы аккаунта."""
    return HttpResponse('Ok')


def job_search_view(request):
    """Отображение шаблона страницы поиска вакансий."""
    return render(request, "job_search.html")


def job_search(request):
    """Обработка запроса поиска вакансий (возможно, дубликат job_search_view)."""
    return HttpResponse('Ok')


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
    return HttpResponse('Ok')


def client_in_networking_view(request):
    """Отображение шаблона страницы клиента в нетворкинге."""
    return HttpResponse('Ok')


def goal_view(request):
    """Отображение шаблона страницы целей."""
    return HttpResponse('Ok')
