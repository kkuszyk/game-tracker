import json


with open("games.json", "r") as file:
    games = json.load(file)


def search_game(games, title):

    for game in games:
        if title.lower() == game['title'].lower():
            return game
    else:
        print("Nie odnaleziono gry. Spróbuj ponownie.")


x = input("Find a title:")

game = search_game(games, x)
print(game)
