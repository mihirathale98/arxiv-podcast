import re
import json


def save_paper_data(content, file_path):
    with open(file_path, "w") as f:
        json.dump(content, f)

def load_paper_data(file_path):
    with open(file_path, "r") as f:
        return json.load(f)

def extract_title(text):
    ## extract everything before "Abstract" or "abstract"
    title = re.split(r"(Abstract|abstract)", text)
    if len(title) >= 1:
        title = title[0]
    else:
        title = "No title found"
    return title
