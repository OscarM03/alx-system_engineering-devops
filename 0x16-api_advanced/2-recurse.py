#!/usr/bin/python3
"""
using Reddit API
"""
import requests


def recurse(subreddit, after=None, hot_list=[]):
    """
    function that queries the Reddit API recursively and returns
    the titles of all posts in a given subreddit
    """
    user = {'User-Agent': 'OscarM'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json'

    params = {'limit': 100}
    if after:
        params['after'] = after

    try:
        response = requests.get(url, headers=user,
                                params=params, allow_redirects=False)
        response.raise_for_status()
        data = response.json()

        posts = data.get('data', {}).get('children', [])
        for post in posts:
            hot_list.append(post['data']['title'])

        after = data.get('data', {}).get('after')
        if after:
            return recurse(subreddit, after, hot_list)
        return hot_list
    except Exception:
        return None
