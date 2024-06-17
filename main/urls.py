"""
URL configuration for spacealien project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views


urlpatterns = [
    path("", views.home_view, name='home'),
    path("account/", views.account_view, name='account'),
    path("account/info/", views.personal_information_view, name='account_info'),
    path("job_search/", views.job_search_view, name='job_search'),
    path("networking/", views.networking_view, name='networking'),
    path("clients/", views.clients_view, name='clients'),
    path("analytics/", views.analytics_view, name='analytics'),
    path("goal/", views.goal_view, name='goal'),
    path("trackers/", views.trackers_view, name='trackers'),
    path("strategies/", views.strategies_view, name='strategies'),
    path("client/networking/", views.client_in_networking_view),
    path("client/job_search/", views.client_in_job_search_view),
]
