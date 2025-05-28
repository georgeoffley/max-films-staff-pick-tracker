import feedparser
from bs4 import BeautifulSoup

FEED_URL = 'https://feeds.simplecast.com/3vVrWdfk'

def get_episodes(feed: str) -> list[str]:
    episodes_from_feed = feed.entries
    
    return episodes_from_feed

def get_episode_content(episode_item: list) -> dict:
    return episode_item.content[0]

def extract_staff_picks_data(episode_item: list, published) -> dict:
    episode_content = get_episode_content(episode_item)
    soup = BeautifulSoup(episode_content.value, 'html.parser')

    # Text is _usually_ wrapped in a <p> tag and we can find it using the <strong>
    #  tag that contains the text "Staff Picks"
    staff_picks_text = soup.find('strong', string='Staff Picks')

    # Not all episodes have a staff picks section
    if staff_picks_text:
        # Finds the block where the relevant text is and returns the parent
        pick_html_block = staff_picks_text.find_parent('p')
        return {
            'published': published,
            'staff_picks_html': pick_html_block
        }

def main():
    # Get Feed
    feed_res = None
    try:
        feed_res = feedparser.parse(FEED_URL)
    except:
        raise Exception("Error fetching feed results")

    # Get episodes from feed
    episodes_from_feed = get_episodes(feed_res)

    staff_picks_episode_block = {}

    for episode in episodes_from_feed:
        staff_picks_episode_block[episode.title] = extract_staff_picks_data(episode_item=episode, published=episode.published)

    # TODO: Create edge case for staff picks that aren't labeled as "Staff Picks"
    # TODO: Parse out staff picks from staff_picks_episode_blocks 
    # TODO: Come up with the data schema
    # TODO: Clean up the data that was parsed for adding to a database

    print(staff_picks_episode_block)

if __name__ == "__main__":
    main()

# Steps for this app (first iteration)
# 1. Start app and fetch the rss feed
# 2. Loop through each episode
#   a. Parse the staff picks
#   b. Make them a pretty list with date, episode, and each pick should have the staff name, move, and if available, the provided movie link
#   c. Print the list of staff picks for each episode