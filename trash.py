import requests
from bs4 import BeautifulSoup
import xlsxwriter

OUT_XLSX_FILENAME = 'out.xlsx'

def parse_urls():
    URL = "https://topbrokers.com/choosing-a-broker"

    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    page_lang = []
    ul = soup.find("ul", class_="language__list")

    url = []
    div = soup.find("div", class_="table-brokers__container clearfix")
    li = div.find_all("li")

    for i in ul:
        url_page = i.find("a", class_="language__list__item__link", href=True)["href"].strip()
        url_page = "https:" + url_page
        page_lang.append(url_page)
        for ind in li:
            try:
                url1 = ind.find("a")["href"].strip()
                url1 = "https://topbrokers.com/choosing-a-broker" + url1
            except: continue
            url.append(url1)
    return url


def dump_to_xlsx(filename, url):

    with xlsxwriter.Workbook(filename) as workbook:
        ws = workbook.add_worksheet()
        bold = workbook.add_format({'bold': True})

        headers = ['Адрес брокера:']

        for col, h in enumerate(headers):
            ws.write_string(0, col, h, cell_format=bold)

        for row, item in enumerate(url, start=1):
            ws.write_string(row, 0, item)



def main():
    parse_urls()
    dump_to_xlsx(OUT_XLSX_FILENAME, parse_urls())

if __name__ == '__main__':
    main()
