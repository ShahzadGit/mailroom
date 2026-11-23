import csv
import sys


def read_subscribers(path):
    with open(path, newline="", encoding="utf-8") as file:
        return list(csv.DictReader(file))


def count_total(subscribers):
    return len(subscribers)


def count_by_group(subscribers):
    counts = {}
    for subscriber in subscribers:
        group = subscriber["group"]
        counts[group] = counts.get(group, 0) + 1
    return counts


def main():
    if len(sys.argv) < 2 or sys.argv[1] != "subscribers":
        print("Usage: uv run mailroom.py subscribers")
        return

    subscribers = read_subscribers("data/subscribers.csv")
    print(f"Total: {count_total(subscribers)}")
    for group, count in count_by_group(subscribers).items():
        print(f"{group}: {count}")


if __name__ == "__main__":
    main()
