#!/usr/bin/python3
"""
using Reddit API
"""
import requests


def top_ten(subreddit):
    """
    function that queries the Reddit API and returns
    the  first 10 hot posts titles
    """
    user = {'User-Agent': 'OscarM'}
    url = 'https://www.reddit.com/r/{}/hot.json'.format(subreddit)

    try:
        response = requests.get(url, headers=user, allow_redirects=False)
        data = response.json()
        posts = data['data']['children']
        for i in range(10):
            print(posts[i]['data']['title'])
    except Exception:
        print("None")
