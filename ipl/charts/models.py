from django.db import models

# Create your models here.

class Match(models.Model):

    id = models.IntegerField(primary_key=True)
    season = models.CharField(max_length=5)
    city = models.CharField(max_length=10)
    date = models.DateField()
    team1 = models.CharField(max_length=10)
    team2 = models.CharField(max_length=10)
    toss_winner = models.CharField(max_length=10)
    toss_decision = models.CharField(max_length=10)
    result = models.CharField(max_length=10)
    dl_applied = models.CharField(max_length=10)
    winner = models.CharField(max_length=10, null=True)
    win_by_runs = models.IntegerField()
    win_by_wickets = models.IntegerField()
    player_of_match = models.CharField(max_length=10)
    venue = models.CharField(max_length=10)
    umpire1 = models.CharField(max_length=10, null=True)
    umpire2 = models.CharField(max_length=10, null=True)
    umpire3 = models.CharField(max_length=10, null=True)

    def __str__(self) -> str:
        return str(self.id)
