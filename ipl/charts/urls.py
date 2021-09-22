from .views import economicalBowler, extra_runs_by_teams, extraRunsByTeams, matchesWonPerYear, number_of_matches_played, numberOfMatchesPlayed, top_economical_bowlers, won_matches_per_year
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('json/matches_played/', number_of_matches_played, name='matches_played_json'),
    path('json/matches_win/', won_matches_per_year, name='won_matches_json'),
    path('json/extra_runs/<str:year>', extra_runs_by_teams, name='extra_runs_json'),
    path('json/top_economic_bowler/<str:year>', top_economical_bowlers, name='economic_bowlers_json'),

    path('matches_played/', numberOfMatchesPlayed, name='matches_played'),
    path('matches_win/', matchesWonPerYear, name='won_matches'),
    path('extra_runs/', extraRunsByTeams, name='extra_runs'),
    path('top_economical_bowler/', economicalBowler, name='economic_bowlers')
]