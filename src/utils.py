import re

def extract_title(text):
    ## extract everything before "Abstract" or "abstract"
    title = re.split(r"(Abstract|abstract)", text)
    if len(title) >= 1:
        title = title[0]
    else:
        title = "No title found"
    return title
