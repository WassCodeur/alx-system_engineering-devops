#!/usr/bin/python3
"""
The module requestes allow us to send httprequests using python
"""

import requests


def top_ten(subreddit):
    """
    print the titles of the 10 hot posts

    args:

    subreddit(str)

    return

    None
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    hders = {"User-Agent": "Custom User Agent"}
    prms = {"limit": 10}
    res = requests.get(url, headers=hders, params=prms, allow_redirects=False)
    if res.status_code == 200:
        to_json = res.json()
        posts = to_json['data']['children']
        for post in posts:
            title = post['data']['title']
            print(title)
     elif res.status_code == 404:
        print(None)
