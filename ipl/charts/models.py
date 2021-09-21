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

class Delivery(models.Model):

    match_id = models.IntegerField()
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    inning = models.IntegerField()
    batting_team = models.CharField(max_length=10)
    bowling_team = models.CharField(max_length=10)
    over = models.IntegerField()
    ball = models.IntegerField()
    batsman = models.CharField(max_length=10)
    non_striker = models.CharField(max_length=10)
    bowler = models.CharField(max_length=10)
    is_super_over = models.BooleanField()
    wide_runs = models.IntegerField()
    bye_runs = models.IntegerField()
    legbye_runs = models.IntegerField()
    noball_runs = models.IntegerField()
    penalty_runs = models.IntegerField()
    batsman_runs = models.IntegerField()
    extra_runs = models.IntegerField()
    total_runs = models.IntegerField()
    player_dismissed = models.CharField(max_length=10, null=True)
    dismissal_kind = models.CharField(max_length=10)
    fielder = models.CharField(max_length=10)