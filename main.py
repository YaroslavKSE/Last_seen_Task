import requests
import json

# API endpoint URL
url = "https://sef.podkolzin.consulting/api/users/lastSeen"

# Parameters
params = {'offset': 0}


def show_20_users(offset):
    # Sending GET request and saving the response as a response object
    response = requests.get(url, params=offset, headers={'accept': 'application/json'})

    # Checking if the request was successful
    if response.status_code == 200:
        # Parse JSON response
        json_data = json.loads(response.text)

        # Extracting the list of users from JSON data
        user_list = json_data['data']

        # Loop through each user in the list
        for user in user_list:
            print("----------")
            if user['isOnline']:
                print(f"{user['nickname']} is online")
            else:
                print(f"{user['nickname']} is offline")


while params['offset'] < 217:
    show_20_users(params)
    params['offset'] += 20
