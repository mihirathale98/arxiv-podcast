import streamlit as st
from src.get_paper import get_paper
from src.pdf_parser import parse_pdf
from src.utils import extract_title



st.title("ArXiv Podcast")

paper_url = st.text_input("ArXiv Paper URL")
search = st.button("Search")

if search:
    if paper_url:
        save_path = get_paper(paper_url)
        content = parse_pdf(save_path)
        st.write(title)
