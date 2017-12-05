import requests
import grequests


# Download pages via gevent jobs
def download_parallel(urls):
    jobs = [grequests.get(url) for url in urls]
    pages = grequests.map(jobs)
    print [len(page.text) for page in pages]


urls = [
    'https://en.wikipedia.org',
    'https://wiki.hackerspaces.org',
    'https://www.noisebridge.net',
    'https://www.eff.org',
    'https://www.lkml.org',  # !
]
download_parallel(urls)
