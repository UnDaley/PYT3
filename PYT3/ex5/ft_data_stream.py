import random
import typing

PLAYERS: list[str] = ['alice', 'bob', 'charlie', 'dylan']
ACTIONS: list[str] = ['run', 'eat', 'sleep', 'grab', 'move', 'climb',
                      'swim', 'release', 'use']


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    while True:
        yield (random.choice(PLAYERS), random.choice(ACTIONS))


def consume_event(
        events: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(events) > 0:
        yield events.pop(random.randrange(len(events)))


def main() -> None:
    print("=== Game Data Stream Processor ===")
    stream = gen_event()
    for i in range(1000):
        name, action = next(stream)
        print(f"Event {i}: Player {name} did action {action}")

    events: list[tuple[str, str]] = []
    for _ in range(10):
        events.append(next(stream))
    print(f"Built list of {len(events)} events: {events}")

    for event in consume_event(events):
        print(f"Got event from list: {event}")
        print(f"Remains in list: {events}")


if __name__ == "__main__":
    main()
