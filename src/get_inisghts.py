from src.gemini_api import GeminiAPI
from src.prompts import insight_extractor_prompt
from src.utils import extract_title

gemini_api = GeminiAPI()


def get_page_insight(title, text, prev_page_summary):
    prompt = insight_extractor_prompt.format(
        title=title, prev_page_summary=prev_page_summary, page_text=text
    )
    response = gemini_api.generate(prompt)
    return response


def get_paper_insights(content):
    title = extract_title(content[0]['page_text'])

    for page_no, page_data in content:
        page_text = page_data['page_text']
        prev_page_summary = content[page_no]['page_text'] if page_no > 0 else 'This is the first page of the paper so there is no previous page summary'
        insights = get_page_insight(title, page_text, prev_page_summary)
        print(insights)

