import random


def main() -> None:
    """Main function to demonstrate list and dict comprehensions."""
    print("=== Game Data Alchemist ===\n")

    players = [
            'Alice', 'bob',
            'Charlie', 'dylan',
            'Emma', 'Gregory',
            'john', 'kevin', 'Liam'
            ]
    print(f"Initial list of players: {players}")

    capitalized_players = [player.capitalize() for player in players]
    print(f"New list with all names capitalized: {capitalized_players}")

    capitalized_only_players = [player for player in capitalized_players
                                if player in players]
    print(f"New list of capitalized names only: {capitalized_only_players}\n")

    score_dict = {player: random.randint(0, 1000)
                  for player in capitalized_players}
    print(f"Score dict: {score_dict}")

    average_score = sum(score_dict[player]
                        for player in score_dict) / len(score_dict)
    print(f"Score average is {round(average_score, 2)}")

    high_scores = {player: score_dict[player]
                   for player in score_dict
                   if score_dict[player] > average_score}
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
