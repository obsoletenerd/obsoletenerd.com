AUTHOR = 'ObsoleteNerd'
SITENAME = 'ObsoleteNerd.com'
SITEURL = "https://obsoletenerd.com"

PATH = "content"
PAGE_PATHS = ["../pages"]

THEME = "themes/obsoletenerd"
TIMEZONE = 'Australia/Melbourne'

DEFAULT_LANG = 'en'

# Feed generation
FEED_ALL_ATOM = 'feeds/feed.atom.xml'
FEED_ALL_RSS = 'feeds/feed.rss.xml'

# Blogroll
LINKS = (
    ("Ballarat Hackerspace", "https://ballarathackerspace.org.au/", "Home away from home"),
    ("Amateur Engineering", "https://amateurengineering.com.au/", "Hacker/Maker webring"),
    ("obsolete.bsky.social (Bluesky)", "https://bsky.app/profile/obsolete.bsky.social", "Occasional project pics"),
    ("@sen@hackerspace.au (Mastadon)", "https://hackerspace.au/@sen", "Similar to above"),
    ("@obsoletenerd (Github)", "https://github.com/obsoletenerd/", "Terrible terrible code"),
    ("@obsoletenerd (Printables)", "https://www.printables.com/@ObsoleteNerd", "3D printable objects by me"),
)

DEFAULT_PAGINATION = 20

from datetime import datetime, timedelta

def days_since(date):
    return (datetime.now().date() - date.date()).days

JINJA_FILTERS = {
    'days_since': days_since
}
