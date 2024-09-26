import os
import streamlit as st

from src.get_paper import get_paper
from src.pdf_parser import parse_pdf
from src.get_inisghts import get_paper_insights
from src.utils import save_paper_data, load_paper_data
from src.get_podcast import get_all_pages_podcast, merge_podcast
from src.get_speech import TTS_Wrapper
from concurrent.futures import ThreadPoolExecutor
import asyncio
from src.speech_processor import process_podcast

if 'tts_wrapper' not in st.session_state:
    st.session_state.tts_wrapper = TTS_Wrapper()


st.title("ArXiv Podcast")

paper_url = st.text_input("ArXiv Paper URL")
search = st.button("Search")

if search:
    if paper_url:
        paper_id = paper_url.split("/")[-1]
        os.makedirs(f"data/{paper_id}", exist_ok=True)

        if os.path.exists(f"data/{paper_id}/parsed_pdf.json"):
            content = load_paper_data(f"data/{paper_id}/parsed_pdf.json")
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

        # concatenated_wav = asyncio.run(process_podcast(merged_podcast, st.session_state.tts_wrapper))
    
        # # Play or save the concatenated_wav as needed
        # st.audio(concatenated_wav, format='audio/wav', sample_rate=24000)

        wavs = []
        for i in range(len(merged_podcast)):
            speaker = merged_podcast[i]['speaker']
            if speaker == 'host':
                speaker = 'Gracie Wise' 
            elif speaker == 'co-host':
                speaker = 'Aaron Dreschner'
            text = merged_podcast[i]['text']
            wav = st.session_state.tts_wrapper.generate_speech(text, speaker)
            wavs.append(wav)

        concatenated_wav = st.session_state.tts_wrapper.concatenate_wavs(wavs)

        st.audio(concatenated_wav, format="audio/wav", sample_rate=24000)
