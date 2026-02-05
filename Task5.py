# Task 5: Fetch user info from a public API (e.g., GitHub user profile endpoint).
import requests
def fetch_github_user(username):
    url = f"https://api.github.com/users/Tisha-0819"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "login": data["login"],
            "name": data.get("name"),
            "public_repos": data["public_repos"],
            "followers": data["followers"],
            "following": data["following"]
        }
    else:
        raise Exception(f"Failed to fetch user data: {response.status_code}")
    
def main():
    username = "octocat"  # Example GitHub username
    try:
        user_info = fetch_github_user(username)
        print("GitHub User Info:")
        for key, value in user_info.items():
            print(f"{key}: {value}")
    except Exception as e:
        print(str(e))
        
if __name__ == "__main__":
    main()
    