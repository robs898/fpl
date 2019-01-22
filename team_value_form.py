from __future__ import division
import requests
import operator
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

url = 'https://fantasy.premierleague.com/drf/bootstrap-static'

resp = requests.get(url=url)
data = resp.json()

team = [190,
        88,
        246,
        484,
        425,
        195,
        221,
        302,
        465,
        391,
        253,
        504,
        437,
        493,
        23
        ]


final_team = {}

for player in data['elements']:
    if player['id'] in team:
        vf = player['value_form']
        final_team[player['web_name']] = vf

sorted_team = sorted(final_team.items(), key=operator.itemgetter(1))

for k,v in sorted_team:
    print k, '-', v
