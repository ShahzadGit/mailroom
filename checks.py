from mailroom import read_subscribers, count_total, count_by_group, count_joined_since, next_send_date

subscribers = read_subscribers("data/subscribers.csv")

assert count_total(subscribers) == 24
assert count_by_group(subscribers)["fa"] == 8
assert count_by_group(subscribers)["fsc"] == 8
assert count_by_group(subscribers)["ics"] == 8

assert count_joined_since(subscribers, "2026-11-20", 30) == 7
assert count_joined_since([{"joined_on": "2026-10-21"}], "2026-11-20", 30) == 1

assert next_send_date("2026-11-20") == "2026-12-07"
assert next_send_date("2026-12-07") == "2027-01-04"

print("All checks pass.")
