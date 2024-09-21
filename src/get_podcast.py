from tqdm import tqdm

from src.gemini_api import GeminiAPI
from src.prompts import podcast_generation_prompt
from src.utils import parse_llm_response

gemini_api = GeminiAPI()

MAX_TRIES = 3

def get_page_podcast(paper_title, page_summary, page_no):
    prompt = podcast_generation_prompt.format(
        title=paper_title, page_summary=page_summary, page_no=page_no
    )
    response = gemini_api.generate(prompt)
    return response

def get_all_pages_podcast(paper_title, content):
    for page_no, page_data in tqdm(content.items(), total=len(content), desc="Generating Podcast", position=0):
        page_summary = page_data['page_summary']
        page_podcast = None
        for _ in range(MAX_TRIES):
            print(f"Trying to generate podcast for page {str(page_no)}")
            try:
                response = get_page_podcast(paper_title, page_summary, int(page_no)+1)
                print(response)

                page_podcast = parse_llm_response(response)
                break
            except Exception as e:
                print(e)
        page_data['page_podcast'] = page_podcast
    return content

