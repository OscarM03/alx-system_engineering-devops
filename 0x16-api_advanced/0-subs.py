#!/usr/bin/python3
"""
using Reddit API
"""
import requests


def number_of_subscribers(subreddit):
    """
    function that queries the Reddit API and returns the number of subscribers
    """
    user = {'User-Agent': 'OscarM'}
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    response = requests.get(url, headers=user)
    data = response.json()
    try:
        subscribers = data['data']['subscribers']
        return subscribers
    except Exception:
        return 0
