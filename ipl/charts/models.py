from django.db import models

# Create your models here.

class Match(models.Model):

    id = models.IntegerField()
    season = models.CharField()
    city = models.CharField()
    date = models.DateField()
    team1 = models.CharField()
    team2 = models.CharField()
    toss_winner = models.CharField()
    toss_decision = models.CharField()
    result = models.CharField()
    dl_applied = models.CharField()
    winner = models.CharField(null=True)
    win_by_run = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField()
    venue = models.CharField()
    umpire1 = models.CharField(null=True)
    umpire2 = models.CharField(null=True)
    umpire3 = models.CharField(null=True)

    def __str__(self) -> str:
        return str(self.id)
