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


VALID_ISSUE = """Subject: Admissions 2026-27 open on Monday
Preview: Founding members hear first about the new session.

Hi {{first_name}},

The college opens admissions for 2026-27 on Monday.

[Apply now](https://imcghumak.example/admissions)

IMCG, Humak
Admission Cell

You're getting this because you joined the Admission waitlist.
Unsubscribe: {{unsubscribe_url}}
"""


def test_issue_01_has_no_problems():
    with open("issues/issue-01.md", encoding="utf-8") as file:
        text = file.read()
    assert mailroom.check_issue(text) == []


def test_a_preview_of_91_characters_is_one_problem():
    preview = "Founding members hear first about the new session."
    text = VALID_ISSUE.replace(preview, "x" * 91)
    assert len(mailroom.check_issue(text)) == 1


def test_no_first_name_in_the_body_is_one_problem():
    text = VALID_ISSUE.replace("Hi {{first_name}},", "Hi there,")
    assert len(mailroom.check_issue(text)) == 1


def test_two_links_is_one_problem_even_when_one_starts_http():
    link = "[Apply now](https://imcghumak.example/admissions)"
    text = VALID_ISSUE.replace(link, link + "\n[More](http://imcghumak.example/more)")
    assert len(mailroom.check_issue(text)) == 1


def test_no_footer_and_no_greeting_is_two_problems():
    text = VALID_ISSUE.replace("Hi {{first_name}},\n", "")
    text = text.replace("You're getting this because you joined the Admission waitlist.\n", "")
    text = text.replace("Unsubscribe: {{unsubscribe_url}}\n", "")
    assert len(mailroom.check_issue(text)) == 2


def test_subject_length_counts_what_len_counts_so_an_emoji_with_skin_tone_is_two():
    subject = "\U0001F44D\U0001F3FD Thanks for joining" + "!" * 30
    assert len(subject) == 51
    text = VALID_ISSUE.replace("Admissions 2026-27 open on Monday", subject)
    assert len(mailroom.check_issue(text)) == 1
