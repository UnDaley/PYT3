import random

ACHIEVEMENTS: list[str] = [
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind",
    "Hidden Path Finder",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(6, 8)
    chosen = random.sample(ACHIEVEMENTS, count)
    return set(chosen)


def main() -> None:
    print("=== Achievement Tracker System ===\n")
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    players: list[set[str]] = []
    for name in names:
        achievements = gen_player_achievements()
        players.append(achievements)
        print(f"Player {name}: {achievements}")

    distinct: set[str] = set()
    for achievements in players:
        distinct = distinct.union(achievements)
    print(f"\nAll distinct achievements: {distinct}")

    common = players[0]
    for achievements in players:
        common = common.intersection(achievements)
    print(f"\nCommon achievements: {common}\n")

    i = 0
    while i < len(players):
        others: set[str] = set()
        j = 0
        while j < len(players):
            if j != i:
                others = others.union(players[j])
            j += 1
        print(f"Only {names[i]} has: {players[i].difference(others)}")
        i += 1
    print()

    all_achievements = set(ACHIEVEMENTS)
    i = 0
    while i < len(players):
        missing = all_achievements.difference(players[i])
        print(f"{names[i]} is missing: {missing}")
        i += 1


if __name__ == "__main__":
    main()
