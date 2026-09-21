import random
import typing


def gen_event() -> typing.Generator[tuple, None, None]:
    """Generates an infinite stream of game events as
    (player_name, action) tuples."""
    players = ["alice", "bob", "charlie", "dylan"]
    actions = ["run", "eat", "sleep", "grab", "move", "climb", "swim"]
    while True:
        name = random.choice(players)
        action = random.choice(actions)
        yield (name, action)


def consume_event(events: list) -> typing.Generator[tuple, None, None]:
    """Consumes events from a list, yielding one at a time
    and removing it from the list."""
    while events:
        event = random.choice(events)
        events.remove(event)
        yield event


def main() -> None:
    """Main function to demonstrate the event generator and consumer."""
    print("=== Game Data Stream Processor ===")
    event_generator = gen_event()
    for i in range(1000):
        event = next(event_generator)
        print(f"Event {i}: Player {event[0]} did action {event[1]}")

    events_list = []
    for _ in range(10):
        events_list += [next(event_generator)]
    print("Built list of 10 events:", events_list)

    for event in consume_event(events_list):
        print("Got event from list:", event)
        print("Remains in list:", events_list)


if __name__ == "__main__":
    main()
