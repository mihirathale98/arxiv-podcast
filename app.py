import os
import streamlit as st

from src.get_paper import get_paper
from src.pdf_parser import parse_pdf
from src.get_inisghts import get_paper_insights
from src.utils import save_paper_data, load_paper_data
from src.get_podcast import get_all_pages_podcast, merge_podcast



st.title("ArXiv Podcast")

paper_url = st.text_input("ArXiv Paper URL")
search = st.button("Search")

if search:
    if paper_url:
        paper_id = paper_url.split("/")[-1]
        os.makedirs(f"data/{paper_id}", exist_ok=True)

        if os.path.exists(f"data/{paper_id}/parsed_pdf.json"):
            parsed_content = load_paper_data(f"data/{paper_id}_insights.json")
        else:
            save_path = get_paper(paper_url)
            content = parse_pdf(save_path)
            save_paper_data(content, f"data/{paper_id}/parsed_pdf.json")
        
        if os.path.exists(f"data/{paper_id}/insights.json"):
            insights = load_paper_data(f"data/{paper_id}/insights.json")
        else:
            insights = get_paper_insights(content)
            save_paper_data(insights, f"data/{paper_id}/insights.json")

        if os.path.exists(f"data/{paper_id}/podcast.json"):
            podcast = load_paper_data(f"data/{paper_id}/podcast.json")
        else:
            podcast = get_all_pages_podcast(paper_id, insights)
            save_paper_data(podcast, f"data/{paper_id}/podcast.json")

        if os.path.exists(f"data/{paper_id}/merged_podcast.json"):
            merged_podcast = load_paper_data(f"data/{paper_id}/merged_podcast.json")['merged_podcast']
        else:
            merged_podcast = merge_podcast(podcast)
            save_paper_data({"merged_podcast":merged_podcast}, f"data/{paper_id}/merged_podcast.json")

        st.write(merged_podcast)