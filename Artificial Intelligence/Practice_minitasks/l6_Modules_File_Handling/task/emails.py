import re


def extract_emails(file_content):
    emails = re.findall(r'\S+@\S+', file_content)
    return emails
