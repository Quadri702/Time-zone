from datetime import datetime, timedelta
from countryinfo import CountryInfo
country = input("Enter name of country: ")
time = input("Enter time to be converted in the format(HH:MM): ")  
timezones = CountryInfo(country).timezones()
for timezone in timezones:
    time_difference = timezone.replace("UTC", "")[1:]
    if ":" in time_difference:
        h, m = map(int, time_difference.split(":"))
        td = timedelta(hours=h, minutes=m)
        h1, m1 = map(int, time.split(":") )
        td1 = timedelta(hours=h1, minutes=m1)
        final_time = td1 - td
        print(f"converted time to UTC according to {country}: UTC {final_time}")
        now = datetime.now() - timedelta(hours = 1) + td
        print(f"Current time in {country} : {now.strftime('%H:%M')}")    