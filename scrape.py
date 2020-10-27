import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news')
# print(res.text)
soup = BeautifulSoup(res.text, 'html.parser')
links = soup.select('.storylink')
subtext = soup.select('.subtext')


def sort_stories(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def custom_hn(links, subtext):
    hacker_news = []

    for inx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[inx].select('.score')

        if len(vote):
            votes_count = int(vote[0].getText().replace(' points', ''))
            # print(votes_count)
            if votes_count >= 100:

                hacker_news.append(
                    {'title': title, 'links': href, 'votes': votes_count})

    return sort_stories(hacker_news)


pprint.pprint(custom_hn(links, subtext))
