from mailroom import read_subscribers, count_total, count_by_group

subscribers = read_subscribers("data/subscribers.csv")

assert count_total(subscribers) == 24
assert count_by_group(subscribers)["fa"] == 8
assert count_by_group(subscribers)["fsc"] == 8
assert count_by_group(subscribers)["ics"] == 8

print("All checks pass.")
