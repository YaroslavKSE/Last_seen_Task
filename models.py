import json
from datetime import datetime, timezone

import requests
from dateutil.parser import parse

url = "https://sef.podkolzin.consulting/api/users/lastSeen"

params = {'offset': 0}


def get_20_users(offset):
    # Sending GET request and saving the response as a response object
    response = requests.get(url, params=offset, headers={'accept': 'application/json'})
    if response.status_code != 200:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return []

    # Parse JSON response
    json_data = json.loads(response.text)

    # Extracting the list of users from JSON data
    user_list = json_data['data']

    # Loop through each user in the list
    return user_list


def print_20_users(list_of_users):
    for user in list_of_users:
        print("----------")
        if user['isOnline']:
            print(f"{user['nickname']} is online")
        else:
            last_seen_str = user['lastSeenDate']
            # Convert lastSeenDate string to a datetime object, considering time zone
            last_seen_datetime = parse(last_seen_str)

            # Get the current datetime in UTC
            current_datetime = datetime.now(timezone.utc)

            # Calculate the time delta between now and the last seen date
            time_delta = current_datetime - last_seen_datetime

            # Extract the number of seconds from the time delta
            seconds = time_delta.total_seconds()
            if 0 <= seconds <= 30:
                print(f"{user['nickname']} seen just now")
                continue
            if 31 <= seconds <= 60:
                print(f"{user['nickname']} seen less than a minute ago")
                continue
            if 61 <= seconds <= 3540:
                print(f"{user['nickname']} seen a couple of minutes ago")
                continue
            if 3541 <= seconds <= 7140:
                print(f"{user['nickname']} seen an hour ago")
                continue
            if last_seen_datetime.day == current_datetime.day and seconds > 7141:
                print(f"{user['nickname']} seen today")
                continue
            if last_seen_datetime.day == current_datetime.day - 1 and seconds > 7141:
                print(f"{user['nickname']} seen yesterday")
                continue
            if 1 < current_datetime.day - last_seen_datetime.day <= 7 and seconds > 7141:
                print(f"{user['nickname']} seen this week")
                continue
            else:
                print(f"{user['nickname']} seen long time ago")


while params['offset'] < 217:
    print_20_users(get_20_users(params))
    params['offset'] += 20
