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


def count_words(subreddit, word_list):
    """
    function that queries the Reddit API recursively and returns
    the titles of all posts in a given subreddit
    """
    try:
        hot_list = recurse(subreddit)

        word_counts = {}
        for word in word_list:
            lower_word = word.lower()
            word_counts[lower_word] = 0

        for title in hot_list:
            lower_title = title.lower()
            for word in word_list:
                lower_word = word.lower()
                word_counts[lower_word] += lower_title.count(lower_word)

        for key, value in word_counts.items():
            print(f"{key}: {value}")
    except Exception:
        return None
