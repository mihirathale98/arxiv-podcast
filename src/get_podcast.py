from tqdm import tqdm

from src.gemini_api import GeminiAPI
from src.prompts import podcast_generation_prompt, podcast_unification_prompt
from src.utils import parse_llm_response

gemini_api = GeminiAPI()

MAX_TRIES = 3



def get_page_podcast(paper_title, page_summary, page_no):
    prompt = podcast_generation_prompt.format(
        title=paper_title, page_summary=page_summary, page_no=page_no
    )
    response = gemini_api.generate(prompt, max_tokens=4096)
    return response

def get_all_pages_podcast(paper_title, content):
    for page_no, page_data in tqdm(content.items(), total=len(content), desc="Generating Podcast", position=0):
        page_summary = page_data['page_summary']
        page_podcast = None
        for _ in range(MAX_TRIES):
            print(f"Trying to generate podcast for page {str(page_no)}")
            try:
                response = get_page_podcast(paper_title, page_summary, int(page_no)+1)

                page_podcast = parse_llm_response(response)
                break
            except Exception as e:
                print(e)
        page_data['page_podcast'] = page_podcast
    return content


def merge_podcast(content):
    new_content = {}
    for k, v in content.items():
        new_content[int(k)] = v

    page_1_podcast = new_content[0]['page_podcast']

    for page_no in range(1, len(new_content)):
        page_data = new_content[int(page_no)]
        page_2_podcast = page_data['page_podcast']
        prompt = podcast_unification_prompt.format(podcast_1=page_1_podcast, podcast_2=page_2_podcast)
        for _ in range(MAX_TRIES):
            try:
                merged_podcast = gemini_api.generate(prompt, max_tokens=8192)
                print(merged_podcast)
                merged_podcast = parse_llm_response(merged_podcast)

                break
            except Exception as e:
                print(e)
        page_1_podcast = merged_podcast


    return merged_podcast
        
