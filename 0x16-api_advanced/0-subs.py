#!/usr/bin/python3
""" module contains reddit data parsing function
"""

import requests as req


def number_of_subscribers(subreddit):
    """ function to get send request to redit api
    RETURNS
        0 - when subreddit not string and not valid
        number_of_subscribers - if successful
    """
    if subreddit is None or not isinstance(subreddit, str):
        return 0
    else:
        header = {
                "User-Agent": "Buka alx Project | 2023"
                }
        r = req.get('http://www.reddit.com/r/{}/about.json'
                    .format(subreddit), headers=header)
        return r.json().get("data", {}).get("subscribers", 0)
