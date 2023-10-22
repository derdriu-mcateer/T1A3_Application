from date import accessed_date
from date import date_today
from datetime import datetime

def test_accessed_date():
    global past_date
    with open("date_last_accessed.txt") as f:
        past_date = f.read()
    assert past_date == "2023-10-22"


def test_date_today():
    with open("date_last_accessed.txt", "w") as f:
        current_date = str(datetime.now().date())
        f.write(f"{current_date}")
    assert current_date == "2023-10-22"
