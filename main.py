game = {}

game['title'] = input("Podaj tytuł gry: ")
game['platform'] = input("Podaj platformę: ")
game['hours_played'] = input("Podaj liczbę godzin gry: ")
game['is_completed'] = input("Czy gra została ukończona? ")

print("--- TWOJA GRA ---")
print(f"Tytuł: {game['title']}")
print(f"Platforma: {game['platform']}")
print(f"Czas gry: {game['hours_played']}")
print(f"Ukończona: {game['is_completed']}")