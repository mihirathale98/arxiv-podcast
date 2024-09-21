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

Output:
'''