import requests
from utils import github_api_request, BASE_URL, GITHUB_TOKEN

def create_pull_request(title, body, head, base):
    """Create a pull request on GitHub."""
    url = f"{BASE_URL}pulls"
    payload = {
        "title": title,
        "head": head,
        "base": base,
        "body": body
    }
    headers = {
        "Authorization": f"token {GITHUB_TOKEN}",
        "Accept": "application/vnd.github+json"
    }
    print("Payload:", payload)  # Debug: Print payload
    response = requests.post(url, headers=headers, json=payload)
    try:
        response.raise_for_status()
    except requests.exceptions.RequestException:
        print("Response JSON:", response.json())  # Debug: Print full API error response
        raise
    return response.json()


if __name__ == "__main__":
    PR_TITLE = "Add new feature"
    PR_BODY = "This PR adds a new feature to the project. Please review."
    SOURCE_BRANCH = "feature/add-new-feature"
    TARGET_BRANCH = "main"

    try:
        pr = create_pull_request(PR_TITLE, PR_BODY, SOURCE_BRANCH, TARGET_BRANCH)
        print(f"Pull Request created successfully: {pr['html_url']}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to create Pull Request: {e}")
