from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "https://sportpesa.com"
page = urlopen(url)
html = page.read().decode("utf-8")
soup = BeautifulSoup(html, "html.parser")
data = soup.body.find_all(class_='event-markets-count-4')

games_arr = []


for i in range(len(data)):
    single_event = data[i].find_all(class_="event-text")
    singe_event_bets =  data[i].find_all(class_="event-selection")
    game_details ={
        "time": single_event[0].text.strip(),
        "game_id": single_event[1].text.strip(),
        "date": single_event[3].text.strip(),
        "home_team": single_event[5].text.strip(),
        "away_team": single_event[6].text.strip(),
        "home_odd": singe_event_bets[0].text.strip(),
        "draw_odd": singe_event_bets[2].text.strip(),
        "away_odd": singe_event_bets[1].text.strip()
    }
    games_arr.append(game_details)

# for index in range(len(singe_event_bets)):
#     print(str(index) +" " + singe_event_bets[index].text.strip())
# print("bets done", len(singe_event_bets))
# for (index) in range(len(single_event)):
#     print(str(index) + " " + single_event[index].text.strip())
    
viable_odds = []
for i in games_arr:
    if float(i['home_odd']) > 1.5 or float(i["draw_odd"]) > 1.5:
        viable_odds.append(i)



sorted_data = sorted(viable_odds, key=lambda x: float(x["home_odd"]), reverse=True)
print(sorted_data)

# print("data", data[0].find_all(class_="event-text"))
# print(data[12].find_all(class_='event-text')[0])


