import requests
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
res = requests.get(url, headers=headers)
print(f'Status code: {res.status_code}')

data = res.json()
repo_dicts = data['items']
print(f"Total repositories: {data['total_count']}")
print(f"Repositories returned: {len(repo_dicts)}")

repo_names, stars, links = [], [], []
for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_dict['name']}</a>"
    links.append(repo_link)

visual_data = [{
    'type': 'bar',
    'x': links,
    'y': stars,
}]
layout = {
    'title': 'Most-Starred Python Projects on Github',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
}
offline.plot({'data': visual_data, 'layout': layout},
             filename='python_repos.html')
