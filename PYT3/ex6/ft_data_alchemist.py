import random


def main() -> None:
    print("=== Game Data Alchemist ===\n")
    players = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory',
               'john', 'kevin', 'Liam']
    print(f"Initial list of players: {players}")

    all_caps = [name.capitalize() for name in players]
    print(f"New list with all names capitalized: {all_caps}")

    only_caps = [name for name in players if name == name.capitalize()]
    print(f"New list of capitalized names only: {only_caps}\n")

    scores = {name: random.randint(0, 1000) for name in all_caps}
    print(f"Score dict: {scores}")

    average = sum([scores[name] for name in scores]) / len(scores)
    print(f"Score average is {round(average, 2)}")

    high = {name: scores[name] for name in scores if scores[name] > average}
    print(f"High scores: {high}")


if __name__ == "__main__":
    main()
