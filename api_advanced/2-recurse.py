#!/usr/bin/python3
""""Doc"""
import requests


def recurse(subreddit, hot_list=[], after=""):
    """"Doc
    Reddit sends an after property in the response.
    Keep retrieving comments until after is null.
    """
    url = "https://www.reddit.com/r/{}/hot.json" \
        .format(subreddit)
    header = {'User-Agent': 'Mozilla/5.0'}
    param = {'after': after}
    res = requests.get(url, headers=header, params=param)

    if res.status_code != 200:
        return None
    else:
        json_res = res.json()
