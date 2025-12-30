import requests
from collections import Counter

def fetch_user_data(username, token=None):
    headers = {"Authorization": f"token {token}"} if token else {}
    user_url = f"https://api.github.com/users/{username}"
    repos_url = f"https://api.github.com/users/{username}/repos?per_page=100&sort=updated"

    user_resp = requests.get(user_url, headers=headers)
    repos_resp = requests.get(repos_url, headers=headers)

    if user_resp.status_code != 200 or repos_resp.status_code != 200:
        return None

    user = user_resp.json()
    repos = repos_resp.json()

    languages = [repo["language"] for repo in repos if repo["language"]]
    lang_count = dict(Counter(languages))

    most_starred = max(repos, key=lambda x: x["stargazers_count"], default={})

    starred_repos = sorted(
        [repo for repo in repos if repo.get("stargazers_count", 0) > 0],
        key=lambda x: x["stargazers_count"],
        reverse=True
    )[:5]

    # Add recent repos (top 5 most recently updated)
    recent_repos = sorted(repos, key=lambda x: x['updated_at'], reverse=True)[:5]

    data = {
        "name": user.get("name") or username,
        "followers": user.get("followers"),
        "following": user.get("following"),
        "public_repos": user.get("public_repos"),
        "top_languages": lang_count,
        "most_starred": {
            "name": most_starred.get("name", ""),
            "stars": most_starred.get("stargazers_count", 0),
            "url": most_starred.get("html_url", "#")
        },
        "starred_repos": [
            {
                "name": repo.get("name", ""),
                "stars": repo.get("stargazers_count", 0),
                "url": repo.get("html_url", "#")
            } for repo in starred_repos
        ],
        "recent_repos": [
            {
                "name": repo.get("name", ""),
                "url": repo.get("html_url", "#"),
                "updated_at": repo.get("updated_at", "")
            } for repo in recent_repos
        ]
    }
    return data
