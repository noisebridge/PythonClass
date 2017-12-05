import requests


# Download pages sequentially
def download_serial(urls):
    pages = [requests.get(url) for url in urls]
    print [len(page.text) for page in pages]


urls = [
    'https://en.wikipedia.org',
    'https://wiki.hackerspaces.org',
    'https://www.noisebridge.net',
    'https://www.eff.org',
    'https://www.lkml.org',
]
download_serial(urls)
