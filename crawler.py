import urllib
from BeautifulSoup import BeautifulSoup

from file_manager import append_to_file

links_to_crawl = set()
crawled_links = set()


def main():
    # site_to_crawl = raw_input('Enter the url you want to crawl: \n')
    links_to_crawl.add('https://barbrothers.com')
    print links_to_crawl
    while links_to_crawl:
        find_urls()


def find_urls():

    global links_to_crawl  # type: set
    global crawled_links  # type: set

    if not links_to_crawl:
        exit(0)
    root = links_to_crawl.pop()
    file_data = urllib.urlopen(root).read()
    soup = BeautifulSoup(file_data)
    for line in soup.findAll('a'):
        links_to_crawl.add(str(line.get('href')))

    links_to_crawl = filter(lambda link: root in link, links_to_crawl)
    print links_to_crawl

if __name__ == '__main__':
    main()
