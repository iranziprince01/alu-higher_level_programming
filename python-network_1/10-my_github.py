#!/usr/bin/python3
"""
    A Python script that takes GitHub credentials
    (username and password) and uses the GitHub API to display the id
"""
import requests
import sys

if __name__ == '__main__':

    r = requests.get('https://api.github.com/user',
                     auth=(sys.argv[1], sys.argv[2]))
    json = r.json()
    try:
        print(json['id'])
    except:
        print("None")
