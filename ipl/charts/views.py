import json

from django.shortcuts import render, HttpResponse
from django.db.models import F
from django.db.models.aggregates import Count

from .models import Match

# Create your views here.
def number_of_matches_played(request, *args):
    '''
    function: This will give you the number of matches played by
    teams in all years
    return: JSON response view.
    '''

    return HttpResponse(None)


# Win Matches view is here
def won_matches_per_year(request, *args):
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
        count = q[3]   # Get the count

        # If year is key in dictionary
        if year in result.keys():

            # If team is key in result[year]
            if team in result[year].keys():
                result[year][team] += count
            else:
                result[year][team] = count

        else:
            result[year] = {team: count}

    return HttpResponse(json.dumps(result))

