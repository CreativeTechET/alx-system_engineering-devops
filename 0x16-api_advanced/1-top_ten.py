#!/usr/bin/python3
"""Contains a function to get top 10 hot posts on reddit"""
import requests as rq


def top_ten(subreddit):
    """Returns Top 10 hottest posts on a given subreddit."""
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "Buka - alx project | 2023"
            }
    params = {
        "limit": 10
    }
    r = rq.get(url, headers=headers, params=params,
               timeout=30, allow_redirects=False)
    if r.status_code == 404:
        print("None")
        return
    results = r.json().get("data")
    [print(i.get("data").get("title")) for i in results.get("children")]
