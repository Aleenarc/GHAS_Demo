import requests
import base64

# GitHub Configuration
GITHUB_TOKEN = "github_pat_11BLUSILY0ZWPmh_ROPcLUYgsRqkG2O7YyCF3MMwnpG59PALyi5itZM28LnXHGCCP3Z6j6AcLqS"  # Replace with your PAT
USERNAME = "Aleenarc"  # Replace with your GitHub username
REPO_NAME = "secret-scanning-demo-simple"
DUMMY_SECRET = "AWS_SECRET_KEY=ABC123FAKEKEY"

# GitHub API URLs
GITHUB_API_URL = "https://api.github.com"
HEADERS = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json",
}

def create_repo():
    """Create a GitHub repository."""
    url = f"{GITHUB_API_URL}/user/repos"
    data = {
        "name": REPO_NAME,
        "private": True,
        "auto_init": True,  # Creates a README.md
    }
    response = requests.post(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print(f"Repository '{REPO_NAME}' created successfully.")
    else:
        print(f"Failed to create repository: {response.status_code}, {response.json()}")

def enable_secret_scanning():
    """Enable secret scanning for the repository."""
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}"
    data = {
        "security_and_analysis": {
            "secret_scanning": {"status": "enabled"}
        }
    }
    response = requests.patch(url, headers=HEADERS, json=data)
    if response.status_code == 200:
        print("Secret scanning enabled successfully.")
    else:
        print(f"Failed to enable secret scanning: {response.status_code}, {response.json()}")

def push_dummy_secret():
    """Push a dummy secret file to the repository."""
    url = f"{GITHUB_API_URL}/repos/{USERNAME}/{REPO_NAME}/contents/dummy_secret.txt"
    encoded_content = base64.b64encode(DUMMY_SECRET.encode()).decode()
    data = {
        "message": "Adding a dummy secret for scanning",
        "content": encoded_content,
    }
    response = requests.put(url, headers=HEADERS, json=data)
    if response.status_code == 201:
        print("Dummy secret pushed successfully.")
    else:
        print(f"Failed to push dummy secret: {response.status_code}, {response.json()}")

def main():
    create_repo()
    enable_secret_scanning()
    push_dummy_secret()

if __name__ == "__main__":
    main()
