import requests
gh_api_repo_search_url = "https://api.github.com/search/repositories"

def create_query(languages, min_stars=50000):
    query = f"stars:>{min_stars} "
    
    for language in languages:
        query += f"language:{language} "
    
    return query

def repos_with_most_stars(languages, min_stars=50000):
    query = create_query(languages, min_stars)
    parameters = {
        "q": query
    }
    
    response = requests.get(gh_api_repo_search_url, params=parameters)
    # print(response.text)
    response_json = response.json()
    print(response_json.keys())
    
    items = response_json["items"]
    return items
    
if __name__ == "__main__":
    languages = ["python", "javascript"]
    results = repos_with_most_stars(languages, 100000)
    
    for result in results:
        print(f"{result['name']} is a {result['language']} repo with {result['stargazers_count']} ")