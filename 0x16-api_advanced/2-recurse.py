#!/usr/bin/python3
""" Module taht contain function recurse """
import requests


def recurse(subreddit, hot_list=[], after=""):
    """ function that queries the Reddit API and returns
    a list containing the titles of all hot articles for
    a given subreddit. If no results are found for the given
    subreddit, the function should return None. """

    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-Agent': 'API Advanced Project by isaacdelahoz'}
    arg1 = {"limit": 100, "after": after}
    resp = requests.get(URL, params=arg1, headers=headers)
    list_a = resp.json().get('data', {}).get('children', None)
    pagination = resp.json().get('data', {}).get('after', None)

    if pagination is not None:
        if list_a:
            for item in list_a:
                hot_list.append(item.get("data").get("title"))
        if pagination is not None:
            recurse(subreddit, hot_list, pagination)
        return hot_list
    else:
        return None
