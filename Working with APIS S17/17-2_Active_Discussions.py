import requests
from operator import itemgetter
import plotly.express as px

# 1. Make an API call to get the IDs of the current top stories
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code for top stories: {r.status_code}")

# This returns a list of hundreds of IDs; we'll just slice the top 30
submission_ids = r.json()
submission_dicts = []

# 2. Loop through the top 30 IDs to get details for each submission
print("Fetching story details... (this may take a few seconds)")
for submission_id in submission_ids[:30]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    response_dict = r.json()

    # Build a dictionary for each article
    # We use .get('descendants', 0) because stories with 0 comments
    # sometimes drop the 'descendants' key entirely from the JSON response
    try:
        submission_dict = {
            'title': response_dict['title'],
            'hn_link': f"https://news.ycombinator.com/item?id={submission_id}",
            'comments': response_dict.get('descendants', 0),
        }
    except KeyError:
        # If an item is dead or deleted, it might be missing a title
        continue

    submission_dicts.append(submission_dict)

# 3. Sort the list of dictionaries by the number of comments in descending order
submission_dicts = sorted(submission_dicts, key=itemgetter('comments'), reverse=True)

# 4. Prepare the data for Plotly
article_links, comment_counts, hover_texts = [], [], []
for submission_dict in submission_dicts:
    # Truncate titles longer than 40 characters so the x-axis doesn't get squished
    title = submission_dict['title']
    short_title = title[:40] + '...' if len(title) > 40 else title

    # Turn the short title into an active HTML link
    article_link = f"<a href='{submission_dict['hn_link']}'>{short_title}</a>"
    article_links.append(article_link)

    comment_counts.append(submission_dict['comments'])
    # Keep the full, un-truncated title for the hover tooltip
    hover_texts.append(title)

# 5. Make the visualization
title = "Most Active Discussions on Hacker News"
labels = {'x': 'Article', 'y': 'Number of Comments'}

fig = px.bar(x=article_links, y=comment_counts, title=title, labels=labels, hover_name=hover_texts)

# Customize the layout and colors (using Hacker News orange!)
fig.update_layout(title_font_size=28, xaxis_title_font_size=16, yaxis_title_font_size=20)
fig.update_traces(marker_color='DarkOrange', marker_opacity=0.8)

fig.show()