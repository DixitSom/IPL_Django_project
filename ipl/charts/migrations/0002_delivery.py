# Generated by Django 2.2 on 2021-09-21 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('charts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('match_id', models.IntegerField()),
                ('inning', models.IntegerField()),
                ('batting_team', models.CharField(max_length=10)),
                ('bowling_team', models.CharField(max_length=10)),
                ('over', models.IntegerField()),
                ('ball', models.IntegerField()),
                ('batsman', models.CharField(max_length=10)),
                ('non_striker', models.CharField(max_length=10)),
                ('bowler', models.CharField(max_length=10)),
                ('is_super_over', models.BooleanField()),
                ('wide_runs', models.IntegerField()),
                ('bye_runs', models.IntegerField()),
                ('legbye_runs', models.IntegerField()),
                ('noball_runs', models.IntegerField()),
                ('penalty_runs', models.IntegerField()),
                ('batsman_runs', models.IntegerField()),
                ('extra_runs', models.IntegerField()),
                ('total_runs', models.IntegerField()),
                ('player_dismissed', models.CharField(max_length=10, null=True)),
                ('dismissal_kind', models.CharField(max_length=10)),
                ('fielder', models.CharField(max_length=10)),
                ('match_ref', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charts.Match')),
            ],
        ),
    ]
