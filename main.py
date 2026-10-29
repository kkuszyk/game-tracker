games = []
answer = "tak"
while answer != "nie":
    game = {}
    game['title'] = input("Podaj tytuł gry: ")
    game['platform'] = input("Podaj platformę: ")
    while True:
        try:
            game['hours_played'] = int(input("Podaj liczbę godzin gry: "))
            break
        except ValueError:
            print("Niepoprawna wartość. Oczekiwana liczba całkowita.")
    game['completed'] = input("Czy gra została ukończona? ").strip().lower()
    while game['completed'] not in ("tak", "nie"):
        print("Niepoprawna wartość. Oczekiwane 'tak' lub 'nie'.")
        game['completed'] = input("Czy gra została ukończona? ").strip().lower()
    games.append(game)
    answer = input("Czy chcesz dodać kolejną grę? [tak/nie] ").strip().lower()
    while answer not in ("tak", "nie"):
        answer = input("Czy chcesz dodać kolejną grę? [tak/nie] ").strip().lower()
print()
print("--- Twoja biblioteka gier ---")
for game in games:
    print("\nTytuł:", game['title'])
    print("Platforma:", game['platform'])
    print("Czas gry:", game['hours_played'])
    print("Gra ukończona:", game['completed'].capitalize())
print()
total_h = 0
for game in games:
    total_h += game['hours_played']
print("Łączny czas spędzony w grach:", total_h)