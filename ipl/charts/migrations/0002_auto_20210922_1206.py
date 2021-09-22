# Generated by Django 2.2 on 2021-09-22 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='delivery',
            name='batsman',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='batting_team',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='bowler',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='bowling_team',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='dismissal_kind',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='fielder',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='non_striker',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='delivery',
            name='player_dismissed',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='city',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='dl_applied',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='player_of_match',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='result',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='team1',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='team2',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='toss_decision',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='toss_winner',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='umpire1',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='umpire2',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='umpire3',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='match',
            name='venue',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='match',
            name='winner',
            field=models.CharField(max_length=255, null=True),
        ),
    ]