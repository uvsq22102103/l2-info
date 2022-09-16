import calendar, datetime
date = (2000,1,32)
try:
    newDate = datetime.date(year=date[0],month=date[1],day=date[2])
    print(newDate)
except:
    print("Cette date n'est pas valide")

jours_mois = calendar.monthrange(date[0], date[1])[1]
bissextile = (not date[0] % 4 and date[0] % 100) or not date[0] % 400
print("Il y a",jours_mois,"jours dans ce mois")
if bissextile:
    print("L'an",date[0],"est bissextile")