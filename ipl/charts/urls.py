from .views import won_matches_per_year
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('/json/matches_win', won_matches_per_year)
]