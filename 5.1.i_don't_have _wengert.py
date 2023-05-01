from datetime import datetime, timedelta
import datetime
import random as rand


def get_last_date():
    while 1:
        try:
            last_date = input("Please enter the last date (YYYY-MM-DD): ")
            last_date = datetime.datetime.strptime(last_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date, you can try again!")
        else:
            return last_date


def get_first_date():
    while 1:
        try:
            first_date = input("Please enter the first date (YYYY-MM-DD): ")
            first_date = datetime.datetime.strptime(first_date, "%Y-%m-%d")
        except ValueError:
            print("Invalid date, you can try again!")
        else:
            return first_date


def get_random_date(date1, date2):
    delta = date2 - date1
    random_days = rand.randint(0, delta.days)
    random_date = date1 + timedelta(days=random_days)

    return random_date


def display_final_date(date):
    if date.weekday() == 0:
        print(f"{date.date()} - I don't have wengert :(")
    else:
        print(date.date())


def main():
    first_date = get_first_date()
    last_date = get_last_date()

    first_date = str(first_date).split(' ')[0]
    last_date = str(last_date).split(' ')[0]

    date1 = datetime.datetime.strptime(first_date, "%Y-%m-%d")
    date2 = datetime.datetime.strptime(last_date, "%Y-%m-%d")

    date = get_random_date(date1, date2)
    display_final_date(date)


if __name__ == '__main__':
    main()
