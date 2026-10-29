games = []
answer = "tak"

while answer != "nie":
    game = {}
    game['title'] = input("Podaj tytuł gry: ")
    game['platform'] = input("Podaj platformę: ")
    game['hours_played'] = int(input("Podaj liczbę godzin gry: "))
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
    if game['completed'] == "tak":
        print("Gra została ukończona.")
    elif game['completed'] == "nie":
        print("Gra nie została jeszcze ukończona.")
    else:
        print("Nie mogę jednoznacznie stwierdzić czy gra została ukończona po wprowadzonej informacji.")
print()

total_h = 0

for game in games:
    total_h += game['hours_played']

print("Łączny czas spędzony w grach:", total_h)