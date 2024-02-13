import re


def extract_urls(file_content):
    urls = re.findall(r'http[s]?://\S+', file_content)
    return urls
