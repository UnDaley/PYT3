import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        if text.count(",") != 2:
            print("Invalid syntax")
            continue
        values: list[float] = []
        valid = True
        for part in text.split(","):
            try:
                values.append(float(part))
            except ValueError as e:
                print(f"Error on parameter '{part}': {e}")
                valid = False
                break
        if not valid:
            continue
        return (values[0], values[1], values[2])


def main() -> None:
    print("=== Game Coordinate System ===")
    print()
    print("Get a first set of coordinates")
    pos1 = get_player_pos()
    print(f"Got a first tuple: {pos1}")
    x1, y1, z1 = pos1
    print(f"It includes: X={x1}, Y={y1}, Z={z1}")
    dist = math.sqrt(x1 ** 2 + y1 ** 2 + z1 ** 2)
    print(f"Distance to center: {round(dist, 4)}")
    print()
    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    x2, y2, z2 = pos2
    dist2 = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(dist2, 4)}")


if __name__ == "__main__":
    try:
        main()
    except (EOFError, KeyboardInterrupt):
        print("\nInput closed, exiting.")
