import os
import requests

# Get environment variables
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")  # Format: owner/repo
PR_NUMBER = os.getenv("PR_NUMBER")

# Debugging (print env variables)
print(f"GITHUB_TOKEN: {'SET' if GITHUB_TOKEN else 'NOT SET'}")
print(f"REPO_NAME: {REPO_NAME}")
print(f"PR_NUMBER: {PR_NUMBER}")

 # Set up GitHub API headers
headers = {"Authorization": f"token {GITHUB_TOKEN}", "Accept": "application/vnd.github.v3+json"}

WELCOME_MESSAGE = """🎉 **Welcome to Open Source, @{username}!** 🎉

Thanks for your first contribution to this project! 🚀  
We appreciate your efforts and look forward to seeing more amazing work from you. 😊

Happy Coding! 💻✨
"""

def get_pr_details():
    """Fetch PR details to get contributor's username"""
    print("hello from get_pr")
    url = f"https://api.github.com/repos/{REPO_NAME}/pulls/{PR_NUMBER}"
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return None

def is_first_time_contributor(username):
    print("hello from is_first_time_contributor")
    """Check if the user has any previous commits in the repository"""
    url = f"https://api.github.com/repos/{REPO_NAME}/commits?author={username}"
    response = requests.get(url, headers=headers)
    commits = response.json()

    return len(commits) == 0  # If no commits found, it's their first time

def post_comment(username):
    """Posts a welcome comment on the PR"""
    url = f"https://api.github.com/repos/{REPO_NAME}/issues/{PR_NUMBER}/comments"
    message = WELCOME_MESSAGE.format(username=username)
    data = {"body": message}

    response = requests.post(url, json=data, headers=headers)
    if response.status_code == 201:
        print(f"✅ Welcome message posted for @{username}")
    else:
        print(f"❌ Failed to post comment: {response.json()}")

if __name__ == "__main__":
    pr_details = get_pr_details()
    if pr_details:
        username = pr_details["user"]["login"]
        post_comment(username)
