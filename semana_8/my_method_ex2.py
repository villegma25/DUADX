import csv

games = [
    {'name': "Grand Theft Auto IV", 'genre': "Action", 'developer': "Rockstar Games", 'rating': "M"},
    {'name': "The Elder Scrolls IV: Oblivion", 'genre': "RPG", 'developer': "Bethesda", 'rating': "M"},
    {'name': "Tony Hawk's Pro Skater 2", 'genre': "Sports", 'developer': "Activision", 'rating': "T"},
]

fieldnames = ['name', 'genre', 'developer', 'rating']

with open('games.tsv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames, dialect='excel-tab')
    
    writer.writeheader()  
    writer.writerows(games)  
