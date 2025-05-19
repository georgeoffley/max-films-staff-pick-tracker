import feedparser
from bs4 import BeautifulSoup

FEED_URL = 'https://feeds.simplecast.com/3vVrWdfk'

def get_episodes(feed: str) -> list[str]:
    episodes_from_feed = feed.entries
    
    return episodes_from_feed

def get_episode_content(episode_item: list) -> dict:
    return episode_item.content[0]

# soup = BeautifulSoup(feed_value_example, 'html.parser')

# print(soup.find_all('p'))

def main():
    # Get Feed
    feed_res = None
    try:
        feed_res = feedparser.parse(FEED_URL)
    except:
        raise Exception("Error fetching feed results")

    # Get episodes from feed
    episodes_from_feed = get_episodes(feed_res)

    # Get content field
    episodes_content = []
    for episode in episodes_from_feed:
        episodes_content.append(get_episode_content(episode))

    # TODO: Parse out episode content to get staff picks
    
    # print(episodes_content)

if __name__ == "__main__":
    main()

# Steps for this app (first iteration)
# 1. Start app and fetch the rss feed
# 2. Loop through each episode
#   a. Parse the staff picks
#   b. Make them a pretty list with date, episode, and each pick should have the staff name, move, and if available, the provided movie link
#   c. Print the list of staff picks for each episode