import requests
import time
import random
import re

log_file = f"results_{time.strftime('%Y%m%d%H%M%S')}.txt"

checked_usernames = set()

with open('usernames.txt', 'r') as file:
    usernames = file.read().splitlines()

random.shuffle(usernames)

with open(log_file, 'w') as log:
    for username in usernames:
        if username in checked_usernames:
            continue

        if re.search(r'[ \-\d]', username): 
            continue

        tiktok_url = f'https://www.tiktok.com/@{username}'

        response = requests.get(tiktok_url)

        if response.status_code == 200:
            result = f'Username @{username} is taken.'
        else:
            result = f'Username @{username} is available.'
            log.write(f'@{username}\n')  

        if "is available" in result:
            print(result)

        checked_usernames.add(username)

        time.sleep(1)
