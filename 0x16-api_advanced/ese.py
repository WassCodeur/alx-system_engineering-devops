import requests

def print_hot_posts(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    headers = {
        "User-Agent": "Custom User Agent"  # Replace with your custom user agent
    }

    params = {
        "limit": 10  # Limit the number of posts to retrieve
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        for post in posts:
            title = post["data"]["title"]
            print(title)
    else:
        print(f"Error: {response.status_code}. Failed to retrieve hot posts.")

print_hot_posts("programming")
