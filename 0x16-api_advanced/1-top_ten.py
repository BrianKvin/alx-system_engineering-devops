#!/usr/bin/python3
"""queries the Reddit API and prints the titles
of the first 10 hot posts listed for a given subreddit."""


def top_ten(subreddit):
    """function that queries the Reddit API and prints the titles
    of the first 10 hot posts listed for a given subreddit."""
    import requests
    import sys

"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'Mozilla/5.0'}
    try:
        response = requests.get(url, headers=headers,
                                allow_redirects=False)
        if response.status_code == 200:
            children = response.json().get('data').get('children')
            for i in range(10):
                print(children[i].get('data').get('title'))
        else:
            print("None")
    except Exception:
        print("None")
"""
    url = 'https://www.reddit.com/r/{}/hot/.json'.format(subreddit)
    headers = {"User-Agent": "ChangeMeClient/0.1 by Makaburi_McMaina"}

    res = requests.get(
            url, headers=headers, allow_redirects=False,
            params={'limit': '10'})

    if res.status_code == 200:
        posts = res.json()
        for post in posts['data']['children']:
            print(post['data']['title'])
    print(None)
