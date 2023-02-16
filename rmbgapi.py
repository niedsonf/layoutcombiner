import requests
import os

def removeBG(file):
    response = requests.post(
        'https://api.remove.bg/v1.0/removebg',
        files={'image_file': open(file, 'rb')},
        data={'size': 'auto', 'crop':'true'},
        headers={'X-Api-Key': ''},
    )

    if response.status_code == requests.codes.ok:
        with open('clean_logo.png', 'wb') as out:
            out.write(response.content)
        with open('clean_logo2.png', 'wb') as out:
            out.write(response.content)
    else:
        print("Error:", response.status_code, response.text)
    return ['clean_logo.png','clean_logo2.png']
