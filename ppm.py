from __future__ import division
import requests
import operator
import sys

reload(sys)  
sys.setdefaultencoding('utf8')

url = 'https://fantasy.premierleague.com/drf/bootstrap-static'

resp = requests.get(url=url)
data = resp.json()

gk = {}
defen = {}
mid = {}
fw = {}
good_players = {}

for player in data['elements']:
    ppm = player['points_per_game']
    if player['minutes'] > 250:
        if float(ppm) > 3.5:
            good_players[player['web_name']] = ppm
            if player['element_type'] == 1:
                gk[player['web_name']] = ppm
            if player['element_type'] == 2:
                defen[player['web_name']] = ppm
            if player['element_type'] == 3:
                mid[player['web_name']] = ppm
            if player['element_type'] == 4:
                fw[player['web_name']] = ppm

sort_gk = sorted(gk.items(), key=operator.itemgetter(1))
sort_defen = sorted(defen.items(), key=operator.itemgetter(1))
sort_mid = sorted(mid.items(), key=operator.itemgetter(1))
sort_fw = sorted(fw.items(), key=operator.itemgetter(1))

for k,v in sorted(good_players.items(), key=operator.itemgetter(1)):
    print k, '-', v
print('   ')
print('GOALKEEPERS')
for k,v in sort_gk:
    print k, '-', v
print('   ')
print('DEFENDERS')
for k,v in sort_defen:
    print k, '-', v
print('   ')
print('MIDFIELDERS')
for k,v in sort_mid:
    print k, '-', v

print('   ')
print('FORWARDS')
for k,v in sort_fw:
    print k, '-', v

