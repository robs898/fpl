from __future__ import division
import requests
import operator
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

url = 'https://fantasy.premierleague.com/drf/bootstrap-static'

resp = requests.get(url=url)
data = resp.json()

team = [468,
        190,
        383,
        247,
        115,
        145,
        43,
        127,
        270,
        122,
        40,
        182,
        437,
        280,
        239
        ]

final_team = {}

for player in data['elements']:
    if player['id'] in team:
        ppm = player['points_per_game']
        cost = float(player['now_cost']) / 10
        value = float(ppm) / cost
        final_team[player['web_name']] = value

sorted_team = sorted(final_team.items(), key=operator.itemgetter(1))

for k,v in sorted_team:
    print k, '-', v
