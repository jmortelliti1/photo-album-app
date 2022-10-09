"""
photo_album_app.py
"""

import sys
import re
import requests

def get_input():
    """Returns a number id input by user."""
    text = input("Please enter an album id number (\"Q\" to quit): ")
    if text == 'Q':
        sys.exit()
    matches = re.findall(r'\d+', text)
    if matches:
        return matches[0]
    else:
        print("Could not find a number to use as an ID.")
        return get_input()

def get_json_response(album_id):
    """Returns json from url constructed with album id"""
    url = 'https://jsonplaceholder.typicode.com/photos'
    params = dict( albumId=album_id )
    response = requests.get(url, params, timeout=5)
    return response.json()

def print_album_titles(json_data):
    """Prints out photo id and title in a readable format."""
    for photo in json_data:
        photo_id = photo['id']
        photo_title = photo['title']
        print(f'[{photo_id}]{photo_title}')

def main():
    """Runs in a loop that quits only when user enters Q."""
    while True:
        album_id = get_input()

        try:
            json_data = get_json_response(album_id)
        except (requests.Timeout, requests.ConnectionError):
            print("There was a connection issue. Please try again.")
            break

        print_album_titles(json_data)

if __name__ == "__main__":
    main()
