import feedparser
from bs4 import BeautifulSoup

FEED_URL = 'https://feeds.simplecast.com/3vVrWdfk'

def get_all_episodes(url: str) -> list[str]:
    d = feedparser.parse(url)
    episodes_from_feed = d.entries

    return episodes_from_feed

def parse_staff_picks(value: str) -> list[str]:
    return 0

# feed_value_example = d.entries[1].content[0]['value'] # Gets the value string which is html and containts our staff picks

# soup = BeautifulSoup(feed_value_example, 'html.parser')

# print(soup.find_all('p'))

def main():
    get_all_episodes(FEED_URL)

if __name__ == "__main__":
    main()

# Steps for this app (first iteration)
# 1. Start app and fetch the rss feed
# 2. Loop through each episode
# 3. Parse the staff picks
# 4. Make them a pretty list with date, episode, and each pick should have the staff name, move, and if available, the provided movie link
# 5. Print the list of staff picks for each episode