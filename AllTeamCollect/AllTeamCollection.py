import tbapy
import csv

tba = tbapy.TBA('')

# currentYear = 2025

# tba.team_years() prints active years, not years since formation
# for key in tba.team(5414).keys():
#     print(key, tba.team(5414)[key]) # :3

# header = ["team number", "city", "state", "zip code", "latitude", "longitude", "rookie year", "2014", "2015", "2016", "2017",
#           "2018", "2019", "2020", "2021", "2022", "2023", "2024", "2025"]
# with open("AllTeamData_years.csv", 'w', encoding="utf-8", newline='') as csvfile:
#     writer = csv.writer(csvfile, delimiter=",")
#     writer.writerow(header)
#     writer.writerows(rows)

# print(tba.team_years(10118))

teams = tba.teams()
rows = []
# state = 1

# print(teams[501].team_number % 5 == 0)
count = 0
for i in teams:
    count+=1
    if count % 5 == 0:
        print(".", end="",flush=True)
    try:
        teamInfo = tba.team(i.team_number)
        if ((not teamInfo["rookie_year"] == None)\
            and (teamInfo["rookie_year"] >= 2014 and teamInfo["state_prov"] == "Texas")):
            # team number, rookie year, city, state, ?competing this year
            row = [teamInfo["team_number"],
                teamInfo["rookie_year"],
                teamInfo["city"],
                teamInfo["state_prov"],
                tba.team_years(i.team_number)[-1] == 2025 if len(tba.team_years(i.team_number)) > 0 else False]
            rows.append(row)
    except Exception as e:
        print(i.team_number, e)

header = ["team number", "rookie year", "city", "state", "competing this year?"]

with open("AllTeamData_years.csv", 'w', encoding="utf-8", newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=",")
    writer.writerow(header)
    writer.writerows(rows)

# final csv: list all the teams that have quit AND all the teams that have been started 2014-2025 -- quit/started = attrition rate


# for i in teams:
#     print(i.team_number)
#     if ("tx" == tba.team_districts(i.team_number)[0]['abbreviation']) :
#         years = tba.team_years(i.team_number)
#         row = []
#         try:
#             started = years[0]
#             last = years[-1]
#             competed = last - started + 1
#             if len(years) != (competed):
#                 for j in range(len(years)):
#                     if years[j+1] > years[j] + 1:
#                         last = years[j]
#                         returned = years[j+1]
#                         break
#             else:
#                 returned = 0
#             years_range = [0] * (2024-2014+1)
#             for play_year in range(2014,2025,1):
#                 if play_year in years:
#                     years_range[play_year-2014] = 1
#                 if started > play_year:
#                     years_range[play_year-2014] = float("nan")
#             row = [i.team_number,i.city, i.state_prov, i.postal_code,i.lat,i.lng, started]
#             row.extend(years_range)
#         except:
#             print(".", end="")
#         rows.append(row)