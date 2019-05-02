from team import names
import requests
import unicodedata

url = 'https://fantasy.premierleague.com/drf/bootstrap-static'

resp = requests.get(url=url)
data = resp.json()

team_value_form = {}

def remove_accents(input_str):
    nfkd_form = unicodedata.normalize('NFKD', input_str)
    only_ascii = nfkd_form.encode('ASCII', 'ignore')
    return only_ascii

for player in data['elements']:
    for first_name, second_name in names.items():
        if remove_accents(player['first_name']) == first_name and remove_accents(player['second_name']) == second_name:
            team_value_form[first_name + ' ' + second_name] = player['value_form']

sorted_team = sorted(team_value_form, key=team_value_form.get, reverse=True)

print('Team value (most valuable first):')
print(sorted_team)



