import tbapy
import csv

import datetime

tba = tbapy.TBA('')

teams = tba.teams()
rows = []

currentYear = datetime.datetime.now().year

rookieYear = 2015

for i in teams:
    if i.team_number % 5 == 0:
        print(".", end="",flush=True)
    try:
        teamInfo = tba.team(i.team_number)
        if ((not teamInfo["rookie_year"] == None)\
            and (teamInfo["rookie_year"] >= rookieYear and teamInfo["state_prov"] == "Texas")):
            # team number, rookie year, city, state, competing this year?
            row = [teamInfo["team_number"],
                teamInfo["rookie_year"],
                teamInfo["city"],
                teamInfo["state_prov"],
                currentYear in tba.team_years(i.team_number)]
            rows.append(row)
    except Exception as e:
        print(i.team_number, e)

header = ["team number", "rookie year", "city", "state", "competing this year?"]

with open("AllTeamData_years.csv", 'w', encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)

# final csv: list all the teams that have quit AND all the teams that have been started 2015-2023 -- quit/started = attrition rate
