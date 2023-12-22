from datetime import datetime

def days_until_new_year(current_date=None):
    if current_date is None:
        current_date = datetime.now()

    next_year_date = datetime(current_date.year + 1, 1, 1)

    days_remaining = (next_year_date - current_date).days

    return days_remaining

if __name__ == "__main__":
    days_left = days_until_new_year()
    print(f"До нового року залишилось {days_left} днів.")
