import json
import requests

def fetch_quote(url):
    try:
        response = requests.get(url)
        if response.status_code != 200:
            print("Invalid quote resource!")
            return

        data = response.json()
        if "content" in data:
            print(data["content"])
        else:
            print("Invalid quote resource!")
    except requests.exceptions.RequestException:
        print("Invalid quote resource!")


if __name__ == "__main__":
    url = input("Input the URL:\n> ")
    fetch_quote(url)
