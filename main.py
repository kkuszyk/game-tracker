game = {}

game['title'] = input("Podaj tytuł gry: ")
game['platform'] = input("Podaj platformę: ")
game['hours_played'] = input("Podaj liczbę godzin gry: ")
game['is_completed'] = input("Czy gra została ukończona? ")

print()
print("--- TWOJA GRA ---")
print(f"Tytuł: {game['title']}")
print(f"Platforma: {game['platform']}")
print(f"Czas gry: {game['hours_played']}")

if game['is_completed'] == "tak":
    print("Gra została ukończona.")
elif game['is_completed'] == "nie":
    print("Gra nie została jeszcze ukończona.")
else:
    print("Nie mogę jednoznacznie stwierdzić czy gra została ukończona po wprowadzonej informacji.")
