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


def main():

    games = []
    answer = "tak"

    while answer != "nie":

        games.append(get_game_data())

        answer = (
            input("Czy chcesz dodać kolejną grę? [tak/nie] ")
            .strip()
            .lower()
        )

        while answer not in ("tak", "nie"):
            answer = (
                input("Czy chcesz dodać kolejną grę? [tak/nie] ")
                .strip()
                .lower()
            )

    print()
    print("--- Twoja biblioteka gier ---")
    print()
    display_game_library(games)

    print("--- Statystyki biblioteki ---")
    print()
    display_game_statistics(*calculate_game_statistics(games))
    print()


if __name__ == "__main__":
    main()
