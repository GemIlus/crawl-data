import requests
from bs4 import BeautifulSoup
import html5lib


# take content of one chapter of novel
def get_content_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    title = soup.find('h2').text.strip()
    content = soup.find('div', class_='book-content mobile-content-padding').text  
    return title, content

# take number chapter of novel
def get_chapter_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links_list = soup.find('div', class_='chapters').find('ul').find_all('a')
    links = [f'http://sachtruyen.net{item["href"]}' for item in links_list]

    return links



#save content into txt file
def save_novel_content(novel_name,url):
    link_chapter = get_chapter_from_url(url)
    data = ""
    num=0
    for link in link_chapter:
        num+=1
        print(num,'/',len(link_chapter))
        title, content = get_content_from_url(link)
        data += title + '\n\n' + content + '\n\n'

        with open('C:/Users/kien bui/OneDrive/Máy tính/crawww/data/'+ novel_name + '.txt', 'w', encoding='utf-8') as file:
            file.write(data)

#take list novel
def get_novel_from_hot(url):
    base_url = 'http://sachtruyen.net'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links_list = soup.find('div', class_='list-content content-mobile-padding').find_all('div', class_='item')
    novels = []
    num = 0

    for link_tag in links_list:
        num += 1
        print(num, '/', len(links_list))
        novel_name, relative_link = link_tag.find('a').text, link_tag.find('a')['href']
        full_link = base_url + relative_link
        novels.append([novel_name, full_link])

    return novels





#crawl everything like you want ^_^

for i in range(0,1):
    url = 'https://sachtruyen.net/danh-sach/tu-khoa?q=tien-hiep&t=category&a=Ti%C3%AAn%20Hi%E1%BB%87p&p=' + str(i)
    novels=get_novel_from_hot(url)
    for novel in novels:
        save_novel_content(novel[0],novel[1])
