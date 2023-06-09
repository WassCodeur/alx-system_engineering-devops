#!/usr/bin/python3
"""
The module requests allow us to send httprequests using python
"""

import requests


def recurse(subreddit, hot_list=None, after=None):
    """
    a function that queries the Reddit API and returns,
    a list containing the titles of all hot articles

    arg:
    subreddit(str)
    hot_list(list)

    return:
    list of all hot articles's titles
    """
    hot_list = []
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    hders = {"User-Agent": "Costum User Agent"}
    prms = {"limit": 100, "after": None}
    res = requests.get(url, headers=hders, params=prms)
    if res.status_code == 200:
        to_json = res.json()
        posts = to_json['data']['children']
        for post in posts:
            title = post['data']['title']
            hot_list.append(title)
        after = to_json['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    elif res.status_code == 404:
        return (None)
