import requests


def fetch_pull_request_authors(owner: str, repo: str, token: str = None):
    """
    Fetch PR contributors from a GitHub repository.
    
    Args:
        owner: GitHub repository owner
        repo: GitHub repository name
        token: Optional GitHub API token for higher rate limits
    
    Returns:
        List of dicts with 'author' and 'prs' keys
    """
    try:
        url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
        headers = {}
        if token:
            headers["Authorization"] = f"token {token}"
        
        # Get all merged PRs
        params = {"state": "all", "per_page": 100}
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        prs = response.json()
        
        # Count PRs by author
        author_counts = {}
        for pr in prs:
            if pr.get("user"):
                author = pr["user"].get("login", "Unknown")
                author_counts[author] = author_counts.get(author, 0) + 1
        
        # Convert to list and sort by PR count
        leaderboard = [
            {"author": author, "prs": count}
            for author, count in author_counts.items()
        ]
        leaderboard.sort(key=lambda x: x["prs"], reverse=True)
        
        return leaderboard
    
    except Exception as e:
        print(f"Error fetching PR leaderboard: {e}")
        return []
