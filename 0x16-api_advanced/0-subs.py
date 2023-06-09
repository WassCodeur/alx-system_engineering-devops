#!/usr/bin/python3
"""
number of subscribes
"""

import requests


def number_of_subscribers(subreddit):
    """
    a function that queries the Reddit
    API and returns the number of subscribers

    args:
    subreddit(str)

    return:
    number of users(int)
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-agent": "Custom User Agent"}
    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code == 200:
        to_json = res.json()
        subscribers = to_json['data']['subscribers']
        return (subscribers)
    else:
        return (0)
