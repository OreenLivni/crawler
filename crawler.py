import urllib
from BeautifulSoup import BeautifulSoup
from time import time
from file_manager import append_to_file, delete_file_if_exists, get_site_name

links_to_crawl = set()
crawled_links = set()
not_crawling = set()
CRAWLED_FILE = 'crawled.txt'
NOT_CRAWLING_FILE = 'not_crawling.txt'


def main():
    global links_to_crawl
    # site_to_crawl = raw_input('Enter the url you want to crawl: \n')
    delete_file_if_exists(CRAWLED_FILE)
    delete_file_if_exists(NOT_CRAWLING_FILE)
    site_to_crawl = 'https://barbrothers.com'
    site_name = get_site_name(site_to_crawl)
    links_to_crawl.add(site_to_crawl)
    start_time = time()
    print 'Time started.'
    while links_to_crawl:
        print links_to_crawl
        find_urls('//'+site_name)
    end_time = time()
    print 'Time ended.'
    print 'The url search took {time}.'.format(time=(end_time - start_time))


def find_urls(root_url):

    global links_to_crawl, crawled_links, not_crawling
    if not links_to_crawl:
        exit(0)
    current_link = links_to_crawl.pop()
    crawled_links.add(current_link)
    file_data = urllib.urlopen(current_link).read()
    soup = BeautifulSoup(file_data)
    for line in soup.findAll('a'):
        link = str(line.get('href'))
        save_url(root_url, link)
        link = link[:-1] if link.endswith('/') else link
        if link not in crawled_links and link not in not_crawling:
            append_to_file(NOT_CRAWLING_FILE, link)
            not_crawling.add(link)
    append_to_file(CRAWLED_FILE, current_link)


def save_url(root_url, url):

    global links_to_crawl, crawled_links
    if url.endswith('/'):
        url = url[:-1]
    if url.startswith('/'):
        url = 'http:'+root_url+url
    if url not in crawled_links and root_url in url:
        links_to_crawl.add(url)


if __name__ == '__main__':
    main()
