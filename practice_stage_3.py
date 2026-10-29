games = [
    {
        "title": "The Witcher 3",
        "platform": "PC",
        "hours_played": 461,
        "completed": True
    },
    {
        "title": "Cyberpunk 2077",
        "platform": "PS5",
        "hours_played": 37,
        "completed": False
    },
    {
        "title": "Minecraft",
        "platform": "PC",
        "hours_played": 2163,
        "completed": False
    }
]

print("Twoja biblioteka gier\n")
for index, game in enumerate(games, start=1):
    print(f"{index}.", {game['title']})
    print("Platforma:", game['platform'])
    print("Czas gry:", game['hours_played'], "godzin")
    if game['completed']:
        print("Ukończona: Tak\n")
    else:
        print("Ukończona: Nie\n")