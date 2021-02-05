#!/usr/bin/python3
""" Module that contain function top_ten """

import requests


def top_ten(subreddit):
    """ function that queries the Reddit API and prints the
    titles of the first 10 hot posts listed for a given subreddit. """

    URL = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'user-agent': 'API Advanced Project by isaacdelahoz'}
    size_query = {"limit": 10}
    r = requests.get(URL, params=size_query, headers=headers).json()
    children = r.get("data", {}).get("children", None)

    if children:
        for topic in children:
            print(topic.get("data").get("title"))
    else:
        print("None")
