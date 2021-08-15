import feedparser
import requests
import datetime

mattermost_url = ''
target_urls = []


def get_feeds(urls):
    feeds = []
    for url in urls:
        feeds.append(feedparser.parse(url))
    return feeds


def create_message(feeds):
    today = datetime.date.today()
    message = []
    message.append(f'## {today:%Y年%m月%d日}の新着情報')
    for f in feeds:
        message.append(f'### [{f.feed.title}]({f.feed.link})')
        for e in f.entries:
            message.append(f'- [{e.title}]({e.link})')
    return '\n'.join(message)


def post_message(message):
    payload = {"text": message}
    r = requests.post(mattermost_url, data=payload)


# print(create_message(get_feeds(target_urls)))
# post_message(create_message(get_feeds(target_urls)))
