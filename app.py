import os
import streamlit as st

from src.get_paper import get_paper
from src.pdf_parser import parse_pdf
from src.get_inisghts import get_paper_insights
from src.utils import save_paper_data, load_paper_data
from src.get_podcast import get_all_pages_podcast



st.title("ArXiv Podcast")

paper_url = st.text_input("ArXiv Paper URL")
search = st.button("Search")

if search:
    if paper_url:
        paper_id = paper_url.split("/")[-1]
        if os.path.exists(f"data/{paper_id}_insights.json"):
            insights = load_paper_data(f"data/{paper_id}_insights.json")
        else: 
            save_path = get_paper(paper_url)
            content = parse_pdf(save_path)
            insights = get_paper_insights(content)
        if insights:
            save_paper_data(insights, f"data/{paper_id}_insights.json")
        podcast = get_all_pages_podcast(paper_id, insights)
        st.write(podcast)
