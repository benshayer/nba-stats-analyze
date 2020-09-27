from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home,name='nba-stats-home' ),
    #path('teams/',views.teams_season_avg, name='nba-teams-stats')
]
