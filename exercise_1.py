import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
response = requests.get(url)

intelligence = {}

characters_name = ["Hulk", "Captain America", "Thanos"]
characters_intelligence = response.json()
for character in characters_intelligence:
    if character['name'] in characters_name:
        intelligence[character["powerstats"]["intelligence"]] = character['name']

sort_int = max(intelligence)
print(f'Самый умный супергерой: {intelligence[sort_int]} - {sort_int}')