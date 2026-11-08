import json


def get_game_data():

    game = {}

    game['title'] = input("Podaj tytuł gry: ")
    game['platform'] = input("Podaj platformę: ")

    while True:
        try:
            game['hours_played'] = int(input("Podaj liczbę godzin gry: "))

            while game['hours_played'] < 0:
                print("Wprowadzono nieprawidłową wartość.")
                game['hours_played'] = int(input("Podaj liczbę godzin gry: "))

            break
        except ValueError:
            print("Niepoprawna wartość. Oczekiwana liczba całkowita.")

    game['completed'] = (
        input("Czy gra została ukończona? ")
        .strip()
        .lower()
    )

    while game['completed'] not in ("tak", "nie"):
        print("Niepoprawna wartość. Oczekiwane 'tak' lub 'nie'.")
        game['completed'] = (
            input("Czy gra została ukończona? ")
            .strip()
            .lower()
        )

    return game


def calculate_game_statistics(games):

    all_games = len(games)

    total_hours = 0
    completed_games = 0
    uncompleted_games = 0

    for game in games:

        total_hours += game['hours_played']

        if game['completed'] == "tak":
            completed_games += 1

        elif game['completed'] == "nie":
            uncompleted_games += 1

    return total_hours, all_games, completed_games, uncompleted_games


def display_game_library(games):

    for game in games:
        print("Tytuł:", game['title'])
        print("Platforma:", game['platform'])
        print("Czas gry:", game['hours_played'])
        print("Gra ukończona:", game['completed'].capitalize())
        print()


def display_game_details(game):

    print("Tytuł:", game['title'])
    print("Platforma:", game['platform'])
    print("Czas gry:", game['hours_played'])
    print("Gra ukończona:", game['completed'].capitalize())


def display_game_statistics(
    total_hours,
    all_games,
    completed_games,
    uncompleted_games
):

    print("Łączny czas spędzony w grach:", total_hours)
    print("Liczba wszystkich gier:", all_games)
    print("Liczba ukończonych gier:", completed_games)
    print("Liczba nieukończonych gier:", uncompleted_games)


def load_games(library):

    try:
        with open(library, "r") as file:
            games = json.load(file)

        return games

    except FileNotFoundError:
        games = []

        return games



def save_games(games, library):

    with open(library, "w") as file:
        json.dump(games, file, indent=4)


def search_game(games, title):

    for game in games:
        if title.lower().strip() == game['title'].lower():
            return game
    else:
        print("Nie odnaleziono gry. Spróbuj ponownie.")


def add_games(games):

    games.append(get_game_data())
    print()
    print("Gra została pomyślnie dodana.")

    while True:

        answer = (
                input("Czy chcesz dodać kolejną grę? [tak/nie] ")
                .strip()
                .lower()
            )

        if answer == "nie":
            break

        elif answer == "tak":
            games.append(get_game_data())
            print()
            print("Gra została pomyślnie dodana.")


def dial_menu():

    print("""
Możliwe akcje:
1 - Wyświetl pełną bibliotekę.
2 - Wyszukaj konkretny tytuł.
3 - Dodaj nowe tytuły do biblioteki.
4 - Wyświetl pełne statystyki gier.
5 - Zapisz obecny stan i zamknij aplikację.
""")


def main():

    print("Próba wczytania biblioteki gier z pliku JSON...")
    print()

    games = load_games("games.json")

    if games:

        print("Biblioteka wczytana poprawnie.")
        print()

    else:

        print("Nie odnaleziono biblioteki.")
        print()
        print("Rozpoczynam proces tworzenia nowej biblioteki.")
        print()
        add_games(games)
        print()

    dial_menu()

    while True:

        try:

            option = int(input("Wybierz opcję: "))

            while option not in (1,2,3,4,5):
                print("Wartość spoza zakresu możliwych opcji. Spróbuj ponownie.")
                option = int(input("Wybierz opcję: "))

        except ValueError:
            print("Nie rozpoznano wartości. Oczekiwana wartość liczbowa. Spróbuj ponownie.")
            option = None

        if option == 1:
            print()
            print("--- Twoja biblioteka gier ---")
            print()
            display_game_library(games)
            dial_menu()

        if option == 2:
            title = search_game(games, input("Podaj tytuł gry: "))

            while title:
                print()
                print("--- Wyszukana gra ---")
                print()
                display_game_details(title)
                print()
                dial_menu()
                break

        if option == 3:
            add_games(games)
            dial_menu()

        if option == 4:
            print()
            print("--- Statystyki biblioteki ---")
            print()
            display_game_statistics(*calculate_game_statistics(games))
            print()
            dial_menu()

        if option == 5:
            save_games(games, "games.json")
            print("Stan biblioteki został zapisany w pliku 'games.json'.")
            break

if __name__ == "__main__":
    main()
