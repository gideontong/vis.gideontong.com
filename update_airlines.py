import re

file_path = "/Users/gideontong/Code/travel.gideontong.com/cards/points/index.html"

with open(file_path, "r") as f:
    content = f.read()

alliances = {
    "aer-lingus": "Independent",
    "aeromexico": "SkyTeam",
    "air-canada": "Star Alliance",
    "flying-blue": "SkyTeam",
    "alaska": "Oneworld",
    "american": "Oneworld",
    "ana": "Star Alliance",
    "avianca": "Star Alliance",
    "british-airways": "Oneworld",
    "cathay": "Oneworld",
    "delta": "SkyTeam",
    "emirates": "Independent",
    "etihad": "Independent",
    "eva": "Star Alliance",
    "finnair": "Oneworld",
    "iberia": "Oneworld",
    "japan-airlines": "Oneworld",
    "jetblue": "Independent",
    "qantas": "Oneworld",
    "qatar": "Oneworld",
    "singapore": "Star Alliance",
    "southwest": "Independent",
    "tap": "Star Alliance",
    "thai": "Star Alliance",
    "turkish": "Star Alliance",
    "united": "Star Alliance",
    "virgin-atlantic": "SkyTeam",
    "virgin-red": "SkyTeam"
}

def replace_airline(match):
    id_val = match.group(1)
    alliance = alliances.get(id_val, "Independent")
    return match.group(0) + f'\n          alliance: "{alliance}",'

content = re.sub(r'id:\s*"([^"]+)",\s*name:\s*"[^"]+",\s*initials:\s*"[^"]+",', replace_airline, content)

with open(file_path, "w") as f:
    f.write(content)

