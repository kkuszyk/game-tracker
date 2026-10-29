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

print("Twoja biblioteka gier:")
for game in games:
    print("\n-", game['title'])
    for k, v in game.items():
        print(f"\t{k}: {v}")