from django.http.response import JsonResponse

from django.shortcuts import render
from django.db.models import F
from django.db.models.aggregates import Count, Sum

from .models import Match, Delivery

# Create your views here.
def number_of_matches_played(request, *args):
    '''
    function: This will give you the number of matches played by
    teams in all years
    return: JSON response view.
    '''

    return JsonResponse(None)


# Win Matches view is here
def won_matches_per_year(request, *args, **kwargs):
    '''
    function: This will give you matches won by teams per year
    return: JSON response view
    '''

    # Query the database 
    query = Match.objects.values_list('winner', 'season').annotate(Count('winner')).order_by('season')
    
    # Final result dictionary
    result = dict()

    # Iterate through the results
    for q in query:
        
        team = q[0]    # Get the team
        year = q[1]    # Get the year
        count = q[2]   # Get the count

        # If year is key in dictionary
        if year in result.keys():

            # If team is key in result[year]
            if team in result[year].keys():
                result[year][team] += count
            else:
                result[year][team] = count

        else:
            result[year] = {team: count}

    return JsonResponse(result)


# Extra runs conceded per team View is here
def extra_runs_by_teams(request, *args, **kwargs):
    '''
    function: It will give you extra runs given by teamin year 2016
    return: JSON response View
    '''
    
    # This is the final result dictionary
    result = dict()

    # Query from database
    query = Delivery.objects.filter(match_ref__season = kwargs['year']).values_list('bowling_team').annotate(Sum('extra_runs')).order_by()

    # Iterate through the results
    for q in query:

        team = q[0]         # Get the Team
        extra_runs = q[1]   # Get Extra Runs

        # If team already in dictionary
        if team in result.keys():
            result[team] += extra_runs
        else:
            result[team] = extra_runs
        
    return JsonResponse(result)
