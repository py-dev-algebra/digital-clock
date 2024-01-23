from datetime import datetime as dt
from dateutil import tz
import time
import os
import locale


def digital_clock(custom_locale: str = 'hr_HR', 
                  time_zone:str = 'Europe/Zagreb') -> str:
    """Function returns curent time in predefined locale and time zone

    Args:
        custom_locale (str, optional): Locale in which will be displayed the name of day in week. Defaults to 'hr_HR'.
        time_zone (str, optional): time in which will be displayed time. Defaults to 'Europe/Zagreb'.

    Returns:
        str: Returns constructed string from datetime object in format: week_day, day.month.year hours:minutes:seconds
    """
    locale.setlocale(locale.LC_TIME, locale=custom_locale)
    custom_tz = tz.gettz(time_zone)
    current_datetime = dt.now().astimezone(custom_tz)
    return f'{current_datetime.strftime("%A").capitalize()}, {current_datetime.strftime("%d.%m.%Y. %H:%M:%S")}'



while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    print(digital_clock(),'\t',digital_clock('de_DE'))
    time.sleep(1)
