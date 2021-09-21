from .views import extra_runs_by_teams, won_matches_per_year
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('json/matches_win/', won_matches_per_year, name='won_matches'),
    path('json/extra_runs/<str:year>', extra_runs_by_teams, name='extra_runs')
]