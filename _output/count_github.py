import requests


GITHUB_USERNAME = "met-ad-688"
url = f"https://github.com/met-ad-688/assignment-01-yasmineelkattan"

try:
    response = requests.get(url)
    response.raise_for_status() 

    repos = response.json()
    print(f"Total GitHub repositories: {len(repos)}")

except requests.exceptions.RequestException as e:
    print(f"Error fetching repositories: {e}")
