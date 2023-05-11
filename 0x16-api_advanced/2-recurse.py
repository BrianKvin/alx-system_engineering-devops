#!/usr/bin/python3
"""queries the Reddit API and returns
 a list containing the titles of all hot articles for a given subreddit. """

import requests


"""def recurse(subreddit, hot_list=[], after="", count=0):
    """Returns a list of titles of all hot posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list"""

def recurse(subreddit, hot_list=[]):
    """queries the Reddit API

    args:
        subreddit - subreddit name

    returns a list containing the titles of all hot articles for a given
    subreddit"""
    global after
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    header = {'User-Agent': 'Title/0.1 by JI-Maina'}
    param = {'after': after}

    res = requests.get(
            url, headers=header, params=param, allow_redirects=False)

    if res.status_code == 200:
        next = res.json().get('data').get('after')
        if next is None:
            after = next
            recurse(subreddit, hot_list)
        list_titles = res.json().get('data').get('children')
        for title in list_titles:
            hot_list.append(title.get('data').get('title'))
        return hot_list
    else:
        return (None)
