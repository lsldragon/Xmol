import requests
from pyquery import PyQuery as pq

content_type = "4"
page = "1"
main_url = "https://www.x-mol.com"
url = "https://www.x-mol.com/news/tag/" + content_type + "?&pageIndex=" + page

response = requests.get(url)
html = response.content

doc = pq(html)
td_lists = doc("#wrapper #main-content #mianBody .newswrap .col1020 .newswrap .col960 .leftnews #newsDiv .newsitem .newslistcot .itemtit a").items()

topic_list = []
url_list = []

for i in td_lists:
    topic_list.append(i.text())
    url_list.append(main_url + i.attr("href"))

date_lists = doc(
    "#wrapper #main-content #mianBody .col960 .leftnews #newsDiv .newsitem .newslistcot .posttiau .newsitem-comment-from span").items()

date_list = []
count = 0
for d in date_lists:
    count = count + 1
    if count % 2 == 0:
        date_list.append(d.text())

content = []
strings = ['topic', 'url', 'date']

for i in range(len(topic_list)):
    d = {}
    d['topic'] = topic_list[i]
    d['url'] = url_list[i]
    d['date'] = date_list[i]

    content.append(d)

print(content)
