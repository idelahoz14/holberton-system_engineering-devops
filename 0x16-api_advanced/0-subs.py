#!/usr/bin/python3
""" Module that conatain function number_of_subscribers """
import requests


def number_of_subscribers(subreddit):
    """ function that queries the Reddit API and returns the number of subscribers
    (not active users, total subscribers) for a given subreddit. If an invalid
    subreddit is given, the function should return 0 """

    if subreddit is None:
        return (0)
    URL = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {'user-agent': 'API Project by andreshugueth'}
    r = requests.get(URL, headers=headers).json()
    subscribers = r.get("data", {}).get("subscribers", 0)
    return subscribers
