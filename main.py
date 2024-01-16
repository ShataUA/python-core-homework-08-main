"""
import some modules
"""
from datetime import date, datetime, timedelta
from collections import OrderedDict


def get_birthdays_per_week(users):
    """
    function for getting dict of targeted birthdays
    """
    today = date.today()
    next_week = today + timedelta(days=6)
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    birthdays_per_week = dict(OrderedDict((weekday, []) for weekday in weekdays))
    if not users:
        return {}
    for user in users:
        name = user['name']
        birthday = user['birthday']
        birthday_this_year = birthday.replace(year=today.year)
        birthday_day_in_week = birthday_this_year.weekday()
        if today.weekday() == 0:
            if birthday_this_year in (today - timedelta(days=1), today - timedelta(days=2)):
                birthdays_per_week['Monday'].append(name)
        if today <= birthday_this_year <= next_week:
            if today.weekday() != 0 and birthday_day_in_week in [5, 6]:
                birthdays_per_week['Monday'].append(name)
            else:
                birthdays_per_week[weekdays[birthday_day_in_week]].append(name)
        elif birthday_this_year < today:
            if today <= birthday.replace(year=today.year + 1) <= next_week:
                new_year_birthday = birthday.replace(year=today.year + 1).weekday()
                if today.weekday() != 0 and new_year_birthday in [5, 6]:
                    birthdays_per_week['Monday'].append(name)
                else:
                    birthdays_per_week[weekdays[new_year_birthday]].append(name)
    if all(user['birthday'].replace(year=today.year) < today for user in users) and all(
            values == [] for values in birthdays_per_week.values()):
        return {}
    congratulations_dict = {key: values for key, values in birthdays_per_week.items() if values}
    return congratulations_dict


if __name__ == "__main__":
    users = [
        {"name": "Jan Koum", "birthday": datetime(2024, 1, 17).date()},
    ]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
