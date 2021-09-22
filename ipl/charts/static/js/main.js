
// This Will plot Number of matches played by teams.
fetch("http://127.0.0.1:8000/json/matches_played/")
  .then(response => response.json())
  .then(data => {
      Highcharts.chart('number-of-matches-played', {
          chart: {
              type: 'column'
          },
          title: {
              text: 'Total Matches played in a Year'
          },
          xAxis: {
              type: 'category',
          },
          yAxis: {
              title: {
                  text: 'Matches Played'
            }
          },
          series: [{
              name: 'Total Matches',
              data: Object.entries(data).sort((a, b) => b[1] - a[1]).slice(0, -1)
          }]
      });
  });


// Extra Runs given by each team in 2016 is here
fetch("http://127.0.0.1:8000/json/extra_runs/2016")
  .then(response => response.json())
  .then(data => {
      Highcharts.chart('extra-runs-for-team', {
          chart: {
              type: 'column'
          },
          title: {
              text: 'Extra Runs Given by Teams in 2016'
          },
          xAxis: {
              type: 'category',
          },
          yAxis: {
              title: {
                  text: 'Extra Runs Given by Teams'
            }
          },
          series: [{
              name: 'Extra Runs',
              data: Object.entries(data).sort((a, b) => b[1] - a[1]).slice(0, 20)
          }]
      });
  });


// Top 10 economic bowlers
fetch("http://127.0.0.1:8000/json/top_economic_bowler/2015")
  .then(response => response.json())
  .then(data => {

    // Some preprocessing Needed
      let series = []
      for (bowler of Object.entries(data)) {
          series.push([bowler[0], bowler[1]])
      }

      Highcharts.chart('economical-bowlers', {
          chart: {
              type: 'column'
          },
          title: {
              text: 'Top 10 Economical bowler of 2015'
          },
          xAxis: {
              type: 'category',
          },
          yAxis: {
              title: {
                  text: 'Economy'
            }
          },
          series: [{
              name: 'Bowlers Economy',
              data: series.sort((a, b) => a[1] - b[1]).slice(0, 10)
          }]
      });
  });


// Matches Wons By Teams in Every Season is here
fetch("http://127.0.0.1:8000/json/matches_win/")
  .then(response => response.json())
  .then(data => {

    // Create a temprary array to store all year and teams
      let all_years = [];
      let all_teams = new Set();

      for (item of Object.entries(data).slice(0, -1)){
            
            for (i of Object.entries(item[1])){
                if(i[0]) {
                    all_teams.add(i[0])
                }
            }
                
            all_years.push(item[0])
        }

    //   To Store all series for plotting
      let series = [];

      for (year of all_years){
          let values = []
          for (team of all_teams){
              values.push(data[year][team])
          }
          values = values.map(value => {
              if (!value){
                  return 0;
              }
              else {
                  return value
              }
          })
          series.push({
              name: `${year}`,
              data: values
          })
      }


      Highcharts.chart('number-of-matches-won', {
          chart: {
              type: 'column'
          },
          title: {
              text: 'Matches Won By Teams in Seasons'
          },
          xAxis: {
              type: 'category',
              categories: [...all_teams]
          },
          yAxis: {
            title: {
                  text: 'Count'
            },
            stackLabels: {
                enabled: true
            }
          },
          plotOptions: {
            column: {
              stacking: 'normal',
              dataLabels: {
                enabled: true
              }
            }
          },
          series: series
      });
  });

  