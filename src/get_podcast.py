import json
from tqdm import tqdm
from src.gemini_api import GeminiAPI
from src.utils import extract_title, parse_llm_response

gemini_api = GeminiAPI('gemini-1.5-pro')


MAX_TRIES = 3

merged_prompt = '''
You are hosting a segment of a technical podcast that focuses on explaining the contents of a research paper. Your goal is to simplify complex concepts while keeping the discussion engaging and intellectually stimulating. Imagine you're speaking with a co-host who will ask clarifying questions.

Context:
- Paper Title: "{title}"
- Current Page Number: {page_no}
- Current Page Insights: {page_summary}
- Previous Podcast Content: {previous_podcast}

Task:
1. If this is the first page (empty previous podcast):
   - Provide a brief introduction to the paper and its topic.
   - Summarize the main points of the current page.

2. If this is not the first page:
   - Seamlessly continue from the previous content.
   - Incorporate new insights from the current page without repeating information.
   - Ensure a smooth transition between the previous content and new information.

3. For all pages:
   - Explain the main points, methodologies, findings, or theories discussed.
   - Include co-host engagement with clarifying questions.
   - Discuss potential real-world applications of the concepts.
   - Provide a quick summary of the most important takeaways.

4. The podcast should be informative, engaging, and suitable for an audience familiar with research but still approachable.

5. The final podcast should be within 800-1000 words.

Guidelines:
- Maintain an approachable, curious, and engaging tone throughout the segment.
- Make the podcast as detailed as possible while keeping it coherent and flowing naturally.
- Do not explicitly mention page numbers.
- Ensure all critical details from both the current page and any previous content are incorporated.
- Avoid omissions, duplications, or inaccurate presentations of information.

The output should be in the following JSON format only:
```
[
  {{"speaker": "host", "text": "text"}},
  {{"speaker": "co-host", "text": "text"}},
  ...
]
```

Podcast:
'''

def generate_podcast(content):
    full_podcast = None
    title = None

    new_content = {}
    for k, v in content.items():
        new_content[int(k)] = v

    content = new_content
    for page_no, page_data in tqdm(content.items(), total=len(content), desc="Generating Podcast", position=0):
        page_summary = page_data['page_summary']
        if page_no == 0:
            title = extract_title(page_summary)
        
        for _ in range(MAX_TRIES):
            print(f"Generating podcast for page {str(page_no)}")
            try:
                prompt = merged_prompt.format(
                    title=title,
                    page_no=page_no,
                    page_summary=page_summary,
                    previous_podcast='This is the first page of the paper so no previous podcast was provided' if full_podcast is None else full_podcast,
                )
                response = gemini_api.generate(prompt, max_tokens=8192)
                full_podcast = parse_llm_response(response)
                break
            except Exception as e:
                print(f"Error generating podcast for page {page_no}: {e}")
        
    return full_podcast