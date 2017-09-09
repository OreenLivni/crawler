import urllib
from BeautifulSoup import BeautifulSoup

from file_manager import append_to_file, delete_file_if_exists

links_to_crawl = set()
crawled_links = set()
CRAWLED_FILE = 'crawled.txt'


def main():
    global links_to_crawl
    # site_to_crawl = raw_input('Enter the url you want to crawl: \n')
    delete_file_if_exists(CRAWLED_FILE)
    site_to_crawl = 'https://barbrothers.com'
    links_to_crawl.add(site_to_crawl)
    while links_to_crawl:
        print links_to_crawl
        find_urls(site_to_crawl.replace('.com', ''))


def find_urls(root_url):

    global links_to_crawl, crawled_links
    if not links_to_crawl:
        exit(0)
    current_link = links_to_crawl.pop()
    crawled_links.add(current_link)
    file_data = urllib.urlopen(current_link).read()
    soup = BeautifulSoup(file_data)
    for line in soup.findAll('a'):
        link = str(line.get('href'))
        if root_url in link and link not in crawled_links:
            links_to_crawl.add(link)
    append_to_file(CRAWLED_FILE, current_link)

if __name__ == '__main__':
    main()
