import requests 
import json

def printRepos(user_id):
    count = 0
    repo_stats = []
    url = "https://api.github.com/users/" + user_id + "/repos"
    request = requests.get(url)
    data = request.json()

    for repo in data:
        url2 = "https://api.github.com/repos/" + user_id + "/" + repo["name"] + "/commits"
        request2 = requests.get(url2)
        count += 1
        commits = len(request2.json())
        repo_stats.append({"Repo":repo["name"], "Commits": commits})
        print("Repo: " + repo["name"] + " Number of commits: " + str(commits))
        if count == 2: break

    git_info = {
        "id": user_id,
        "statusCodeUser": request.status_code,
        "repoCount": count,
        "stats": repo_stats
    } 

    return git_info


user = "allen-best"
printRepos(user)