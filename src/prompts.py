insight_extractor_prompt = '''
"Read the content of the selected page from this research paper and extract all the key insights. Specifically, focus on the following aspects:

Core Research Contributions: Summarize the main ideas, findings, and conclusions presented on the page.

Key Methodologies or Experiments: Highlight any detailed methods, experimental setups, or frameworks discussed. Mention their relevance to the overall research.

Critical Data or Results: Identify any significant statistics, figures, tables, or graphs. If present, explain the importance of these results and their impact on the conclusions.

Theoretical or Conceptual Framework: Extract any theoretical models, hypotheses, or conceptual frameworks mentioned. Clarify how these frameworks guide or support the research.

Important Citations or References: Note any references to prior research or studies that are central to the points made on the page.

Technical Terminology: List and define key technical terms or concepts introduced or elaborated on the page, with emphasis on their application within the research context.

Gaps or Questions Raised: Mention any gaps, limitations, or unanswered questions identified that are relevant to future research directions.

Provide a concise yet detailed summary that includes all these elements while maintaining the original intent of the text."

Additionally you are also provided with the previous page summary to avoid information loss and redundancy.

Do not explicitly mention the page number in the insights.

If it is the first page of the paper, mention the title of the paper.

Title:
{title}

Previous page summary:
{prev_page_summary}

Given page from the paper:
{page_text}

Insights for page {page_no}:
'''


podcast_generation_prompt = '''
You are hosting a segment of a technical podcast that focuses on explaining the contents of a specific page from a research paper. Your goal is to simplify complex concepts while keeping the discussion engaging and intellectually stimulating. Imagine you're speaking with a co-host who will ask clarifying questions. Structure your segment as follows:

Brief introduction: Summarize the topic of the page in 1-2 sentences.
Detailed exploration: Explain the main points, methodologies, findings, or theories discussed on the page.
Co-host engagement: Include moments where your co-host asks clarifying questions.
Real-world application: Briefly discuss how the concepts on this page might apply to practical situations.
Quick summary: Restate the most important takeaways from the page.

Do not explicitly mention the page number.
Make the podcast as detailed as possible.

Maintain an approachable, curious, and engaging tone throughout the segment. Focus on the following insights from page number {page_no} of the research paper titled "{title}":
insights: {page_summary}

The output should be in the following JSON format only, within the quotes:
```
json[
  {{"speaker": "host", "text": "text"}},
  {{"speaker": "co-host", "text": "text"}},
  ...
]
```

Podcast:
'''


podcast_unification_prompt = """
You are tasked with merging two partial segments of a technical podcast discussing a research paper. Your objective is to combine both parts seamlessly, ensuring that no information is omitted or repeated. Follow these guidelines:

1. **Flow and Continuity**: 
   - Ensure the podcast flows naturally, with a conversational tone between the segments.
   - The transition from one segment to the next should be smooth and unnoticeable.

2. **Information Preservation**: 
   - Incorporate all critical details from both segments.
   - Avoid omitting, duplicating, or inaccurately presenting any information from either segment.

3. **Rephrasing and Clarification**: 
   - Rephrase technical points or questions where necessary to improve clarity.
   - If certain areas could benefit from further explanation or elaboration, feel free to expand upon them while remaining true to the original content.

4. **Tone Consistency**: 
   - Maintain a consistent conversational and engaging tone throughout the podcast.
   - Ensure both segments sound cohesive, as if they belong to the same episode, with uniform detail and engagement.

5. **Introduction**:
   - If the first piece of the podcast is missing an introduction, mention the title of the paper and provide a brief introduction to the research topic being discussed.

6. **Detail and Length**:
   - Aim to make the combined podcast as detailed as possible while keeping the total length under 7000 words.
   - The merged podcast should be informative, engaging, and suitable for an audience familiar with research but still approachable.

7. **Output Format**:
   - Maintain the format of the original podcast.
   - Use the following format for the output:
   ```json
   [
     {"speaker" : "host", "text": "text"},
     {"speaker" : "co-host", "text": "text"},
     ...
   ]
   ```


Input Segments:

Piece 1: {podcast_1}
Piece 2: {podcast_2}


Output:
"""