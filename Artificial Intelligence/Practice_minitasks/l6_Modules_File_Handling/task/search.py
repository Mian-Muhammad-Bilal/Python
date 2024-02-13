
def search_keywords(file_content, keyword):
    keyword_count = file_content.lower().count(keyword.lower())
    return keyword_count
