import requests
import plotly.express as px

# 1. Define the programming language you want to search for
# Try changing this to 'ruby', 'c', 'haskell', 'go', or 'java'
language = 'javascript'

# 2. Make an API call and check the response
url = "https://api.github.com/search/repositories"
# We append the query string to search for the language and sort by stars
url += f"?q=language:{language}+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# 3. Process overall results
response_dict = r.json()
print(f"Complete results: {not response_dict['incomplete_results']}")

# 4. Process repository information
repo_dicts = response_dict['items']
repo_links, stars, hover_texts = [], [], []

for repo_dict in repo_dicts:
    # Turn repo names into active HTML links for the chart's x-axis
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)

    # Store the number of stars for the y-axis
    stars.append(repo_dict['stargazers_count'])

    # Build hover texts showing the owner and description
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# 5. Make the visualization
title = f"Most-Starred {language.title()} Projects on GitHub"
labels = {'x': 'Repository', 'y': 'Stars'}

fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

# Customize the layout and colors
fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20)
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6)

# Display the chart in your default web browser
fig.show()