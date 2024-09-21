from tqdm import tqdm

from src.gemini_api import GeminiAPI
from src.prompts import insight_extractor_prompt
from src.utils import extract_title

gemini_api = GeminiAPI()


def get_page_insight(title, text, prev_page_summary, page_no):
    prompt = insight_extractor_prompt.format(
        title=title, prev_page_summary=prev_page_summary, page_text=text, page_no=page_no
    )
    response = gemini_api.generate(prompt)
    return response


def get_paper_insights(content):
    title = extract_title(content[0]['page_text'])

    for page_no, page_data in tqdm(content.items(), total=len(content), desc="Extracting Insights", position=0):
        page_text = page_data['page_text']
        prev_page_summary = content[page_no - 1]['page_summary'] if page_no > 0 else "This is the first page of the paper so no previous page summary was provided"
        insights = get_page_insight(title, page_text, prev_page_summary, page_no+1)
        page_data['page_summary'] = insights        

    return content
