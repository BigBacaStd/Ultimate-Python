import requests


def get_api_response():
    """Make an API call and return the response."""
    url = "https://api.github.com/search/repositories?q=language:python+sort:stars"
    headers = {"Accept": "application/vnd.github.v3+json"}
    r = requests.get(url, headers=headers)
    return r


def get_repo_dicts(r):
    """Return a list of dictionaries representing the most popular repositories."""
    response_dict = r.json()
    return response_dict['items']


# Only run the output if this file is executed directly (not when imported by pytest)
if __name__ == '__main__':
    r = get_api_response()
    print(f"Status code: {r.status_code}")

    repo_dicts = get_repo_dicts(r)
    print(f"Repositories returned: {len(repo_dicts)}")