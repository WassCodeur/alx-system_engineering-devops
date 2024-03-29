#!/usr/bin/python3
"""
The module requests allow us to send httprequests using python
"""

import requests


def recurse(subreddit, hot_list=[], after=None, count=0):
    """
    a function that queries the Reddit API and returns,
    a list containing the titles of all hot articles

    arg:
    subreddit(str)
    hot_list(list)

    return:
    list of all hot articles's titles
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    hders = {"User-Agent": "Costum User Agent"}
    prms = {"limit": 100, "after": None, "count": 0}
    res = requests.get(url, headers=hders, params=prms)
    if res.status_code == 200:
        to_json = res.json()
        posts = to_json['data']['children']
        for post in posts:
            dat = post['data']
            title = dat['title']
            hot_list.append(title)
        after = to_json['data']['after']

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return (None)
