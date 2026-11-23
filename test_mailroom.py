import mailroom


def load_subscribers():
    return mailroom.read_subscribers("data/subscribers.csv")


def test_counts_all_subscribers():
    assert mailroom.count_total(load_subscribers()) == 24


def test_counts_subscribers_in_each_group():
    counts = mailroom.count_by_group(load_subscribers())
    assert counts["fa"] == 8
    assert counts["fsc"] == 8
    assert counts["ics"] == 8


def test_counts_subscribers_who_joined_in_the_window():
    assert mailroom.count_joined_since(load_subscribers(), "2026-11-20", 30) == 7


def test_counts_a_subscriber_who_joined_on_the_first_day_of_the_window():
    subscribers = [{"joined_on": "2026-10-21"}]
    assert mailroom.count_joined_since(subscribers, "2026-11-20", 30) == 1


def test_next_send_date_from_a_mid_month_day():
    assert mailroom.next_send_date("2026-11-20") == "2026-12-07"


def test_next_send_date_from_a_send_day_moves_to_next_month():
    assert mailroom.next_send_date("2026-12-07") == "2027-01-04"
