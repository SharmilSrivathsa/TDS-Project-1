import requests
import pandas as pd
import time

# GitHub Personal Access Token for authenticated requests
GITHUB_TOKEN = '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'
headers = {'Authorization': f'token {GITHUB_TOKEN}'}

# Fetch users located in Basel with more than 10 followers
def get_users(location='Basel', min_followers=10):
    url = f"https://api.github.com/search/users?q=location:{location}+followers:>{min_followers}&per_page=100"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    users = response.json().get('items', [])
    return [user['login'] for user in users]

# Get detailed information for each user
def get_user_details(username):
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Clean and format company names as specified
    company = data.get('company', '')
    if company:
        company = company.strip().lstrip('@').upper()  # Clean up company name

    return {
        'login': data.get('login', ''),
        'name': data.get('name', ''),
        'company': company,
        'location': data.get('location', ''),
        'email': data.get('email', ''),
        'hireable': data.get('hireable', ''),
        'bio': data.get('bio', ''),
        'public_repos': data.get('public_repos', 0),
        'followers': data.get('followers', 0),
        'following': data.get('following', 0),
        'created_at': data.get('created_at', '')
    }

# Get up to 500 repositories for each user
def get_repositories(username):
    repos = []
    page = 1
    while True:
        url = f"https://api.github.com/users/{username}/repos?per_page=100&page={page}"
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        if not data:
            break
        for repo in data:
            # Handle cases where license information may be missing
            license_info = repo.get('license')
            license_name = license_info['key'] if license_info else ''  # Default to empty string if no license

            repos.append({
                'login': username,  # Add the user's login as a reference
                'full_name': repo.get('full_name', ''),
                'created_at': repo.get('created_at', ''),
                'stargazers_count': repo.get('stargazers_count', 0),
                'watchers_count': repo.get('watchers_count', 0),
                'language': repo.get('language', ''),
                'has_projects': repo.get('has_projects', False),
                'has_wiki': repo.get('has_wiki', False),
                'license_name': license_name
            })
        if len(data) < 100 or len(repos) >= 500:
            break
        page += 1
        time.sleep(1)  # Avoid hitting rate limits
    return repos[:500]

# Main function to orchestrate data fetching and saving
def main():
    # Fetch users
    usernames = get_users()
    users_data = []
    repos_data = []

    # Fetch details for each user and their repositories
    for username in usernames:
        user_info = get_user_details(username)
        users_data.append(user_info)

        repos = get_repositories(username)
        repos_data.extend(repos)

    # Save to CSV files
    users_df = pd.DataFrame(users_data)
    repos_df = pd.DataFrame(repos_data)
    users_df.to_csv('users.csv', index=False)
    repos_df.to_csv('repositories.csv', index=False)
    print("Data successfully scraped and saved to users.csv and repositories.csv.")

if __name__ == "__main__":
    main()
