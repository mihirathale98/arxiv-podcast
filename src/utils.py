import re
import json
import re
import ast


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


def parse_llm_response(response):
    match = re.search(r"```json(.*)```", response, re.DOTALL)
    if match:
        return ast.literal_eval(match.group(1))
    else:
        return None