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
You are tasked with merging two partial segments of a technical podcast based on a research paper. Your goal is to seamlessly combine both parts, ensuring that no information is lost or repeated. As you do this, follow these rules:

Flow and Continuity: Ensure the podcast flows naturally, maintaining a conversational tone between the segments. The transition from one segment to the next should be smooth.
Information Preservation: Incorporate all key details from both podcast pieces. Ensure no important information from either segment is missed, duplicated, or inaccurately presented.
Rephrasing and Clarification: Where necessary, rephrase technical points or questions to enhance clarity. If there are areas that could be expanded upon or explained more clearly, feel free to improvise while staying true to the original content.
Tone Consistency: Maintain a conversational and engaging style throughout. Ensure that both segments sound like they belong to the same episode and are delivered with an equal level of detail and engagement.
Once complete, the merged podcast should sound cohesive, informative, and ready for an audience of knowledgeable listeners interested in research, while still being approachable.

Make the merged podcast as detailed as possible. Combine the podcasts to create a cohesive and engaging technical podcast.

Please maintain the format of the merged podcast to the similar format as the original.

Output format should be in the following format:
```json
[{{"speaker" : "host", "text": "text"}}, {{"speaker" : "co-host", "text": "text"}}, ...]
```

Piece 1:
{podcast_1}

Piece 2:
{podcast_2}

Output:
"""