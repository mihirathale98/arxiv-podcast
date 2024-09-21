import requests
import tempfile

def verify_url(url):
    if 'abs' in url:
        return url.replace('abs', 'pdf')
    elif 'html' in url:
        return url.replace('html', 'pdf')
    else:
        return url

def save_paper(response):
    tempfile_ = tempfile.NamedTemporaryFile(suffix='.pdf', delete=False)
    with open(tempfile_.name, 'wb') as f:
        f.write(response.content)
    return tempfile_.name

def get_paper(url):
    url = verify_url(url)
    response = requests.get(url)
    response.raise_for_status()
    file_path = save_paper(response)
    return file_path
