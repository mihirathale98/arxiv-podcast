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
You are hosting a technical podcast, and today, you're going to explain the contents of a specific page from a research paper in a conversational, engaging style. Your goal is to simplify complex concepts while keeping the discussion intellectually stimulating.

Start by introducing the research topic briefly, then dive into the details presented on the given page. Imagine you're speaking with a co-host who will ask clarifying questions along the way. Here is a guide for the structure:

Introduction: Summarize the broader topic of the paper in 2-3 sentences.
Detailed Exploration: Explain the main points, methodologies, findings, or theories discussed on the page in a concise yet detailed manner.
Co-Host Engagement: At key moments, imagine your co-host asks clarifying questions like:
“Can you break that down a little more?”
“What would be a real-world example of this?”
Real-World Application: Discuss how the research or concepts on this page might apply to practical situations or innovations.
Summary: Wrap up by restating the most important takeaways from the page.
Ensure the tone is approachable, curious, and engaging, as though you're explaining it to an audience of intelligent expert listeners.

For this podcast, focus on the following insights from the content of page number {page_no} of the research paper titled "{title}".

insights:
{page_summary}

The output format should be in the following format:
```json
[{{"speaker" : "host", "text": "text"}}, {{"speaker" : "co-host", "text": "text"}}, ...]
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

Please maintain the format of the merged podcast to the similar format as the original.

```json
[{{"speaker" : "host", "text": "text"}}, {{"speaker" : "co-host", "text": "text"}}, ...]
```

Piece 1:
{podcast_1}

Piece 2:
{podcast_2}

Merged Podcast:
"""