import sys


def score_analytics() -> None:
    """Player Score Analytics demonstrating command-line arguments and
    basic statistics."""
    print("=== Player Score Analytics ===")
    scores = []
    args = sys.argv[1:]
    for arg in args:
        try:
            score = int(arg)
            scores += [score]
        except ValueError:
            print(f"Invalid parameter: '{arg}'")
    if len(scores) == 0:
        print("No scores provided. Usage:" +
              " python3 ft_score_analytics.py <score1> <score2> ...")
        return
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {sum(scores)}")
    print(f"Average score: {sum(scores) / len(scores)}")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}\n")


if __name__ == "__main__":
    score_analytics()
