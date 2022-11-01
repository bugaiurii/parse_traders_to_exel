import requests
from bs4 import BeautifulSoup

URL = "https://topbrokers.com/de/choosing-a-broker"

page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")


def url_lang_pars():
    page_lang = []
    ul = soup.find("ul", class_="language__list")

    for i in ul:
        url = i.find("a", class_="language__list__item__link", href=True)["href"].strip()
        url = "https:" + url
        page_lang.append(url)
    print(*page_lang, sep="\n")


def one_page_parse():
    url = []
    div = soup.find("div", class_="table-brokers__container clearfix")
    li = div.find_all("li")
    for i in li:
        try:
            url1 = i.find("a")["href"].strip()
            url1 = "https://topbrokers.com/choosing-a-broker" + url1
        except: continue
        url.append(url1)
    print(*url, sep="\n")




def main():
    one_page_parse()
    #url_lang_pars()


if __name__ == '__main__':
    main()


