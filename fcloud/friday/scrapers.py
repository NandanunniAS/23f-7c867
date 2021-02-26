import wikipedia
import requests, json
from bs4 import BeautifulSoup

from .dictionary import questions, emoji

def get_wiki_data(cmd: str) -> str:
    title = cmd
    for qn in questions:
        title = title.replace(qn, "").strip()
    title = title.replace(" ?", "").replace("?", "")
    try:
        reply = wikipedia.summary(cmd, sentences=2)
    except wikipedia.exceptions.DisambiguationError:
        reply = 'Sorry sir, Which {} are you refering to ?'.format(title.capitalize())
    except wikipedia.exceptions.PageError:
        if 'nandanunni' in title.lower():
            reply = f"It's you ! My boss {emoji.smile_with_teeth}"
        else:
            reply = "Sorry sir, I don't know much about {}".format(title.capitalize())
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it. " + emoji.confused

    return reply


def get_weather_data() -> str:
    try:
        response = requests.get("https://www.google.com/search?q=weather+kollam%2C+kerala&oq=weather")
        html_code = response.content
        html_code = BeautifulSoup(html_code, "html.parser")
        reply = html_code.find("div", {"class", "iBp4i"}).text + ", "
        reply += html_code.find("div", {"class", "tAd8D"}).text.split("\n")[1] + ", "
        reply += html_code.find("div", {"class", "kCrYT"}).text.split(" / ")[0]
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it. " + emoji.confused
    return reply


def get_github_data() -> str:
    try:
        headers = {
            'Authorization': 'token c4bae3938f2e431ac0deb7cb5531aa1faa15cb15',
            "Accept": "application/vnd.github.v3+json"
        }
        res = requests.get('https://api.github.com/users/Nandan-unni/received_events', headers)
        data = json.loads(res.text)
        feeds = []
        for item in data:
            if item['type'] == 'WatchEvent':
                feeds.append(f"{item['actor']['login']} starred {item['repo']['name']}")
            elif item['type'] == 'ForkEvent':
                feeds.append(f"{item['actor']['login']} forked {item['repo']['name']}")
        reply = " [newline] ".join(item for item in feeds[:5])
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it. " + emoji.confused
    return reply


def get_cricket_data() -> str:
    try:
        res = requests.get("https://www.cricbuzz.com/cricket-team/india/2")
        html_code = res.content
        html_code = BeautifulSoup(html_code, "html.parser")
        matches = html_code.find_all("div", {"class", "matchscag"})
        india_upcomings = []
        for match in matches:
            place = match.find("span", {"class", "cb-font-12"}).text
            teams = [team.text for team in match.find_all("div", {"class", "matchscag-name"})]
            date = match.find("div", {"class", "cb-text-preview"}).text
            india_upcomings.append(f"{place}, {teams[0]} vs {teams[1]}, {date}")
        reply = " [newline] ".join(item for item in india_upcomings)
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it. " + emoji.confused
    return reply


def get_my_location() -> str:
    try:
        response = requests.get("http://ipinfo.io/loc")
        reply = [float(cord) for cord in response.text.replace("\n", "").split(",")]
    except requests.exceptions.ConnectionError:
        reply = "Maybe if I had a good internet connection, I could answer it. " + emoji.confused
    return reply

