def calculate_total_hours(*hours):

    total_time = 0

    for time in hours:
        total_time += time

    return total_time


def display_game_info_old(**game):

    for key, value in game.items():
        print(f"{key}: {value}")


def display_game_info_old2(*titles, **params):

    print("--- Podstawowe informacje ---")
    for title in titles:
        print(title)

    print("\n--- Dodatkowe informacje ---")
    for param, param_value in params.items():
        print(f"{param}: {param_value}")

print("--- Twoja biblioteka gier ---")
print()

def display_game_info(title, platform, hours_player=0, completed=False):

    print("Tytuł:", title)
    print("Platforma:", platform)
    print("Czas gry:", hours_player)
    print("Ukończenie gry:", completed)
    print()

display_game_info("Minecraft", "PC", 120, True)
display_game_info(completed=True, hours_player=500, platform="PC", title="Diablo II")
display_game_info("GTA V", hours_player=50, completed=False, platform="PS5")
display_game_info("The Witcher 3", "PS5")
