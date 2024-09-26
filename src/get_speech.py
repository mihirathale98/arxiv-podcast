import torch
from TTS.api import TTS
import numpy as np
from functools import lru_cache

class TTS_Wrapper:
    def __init__(self, language="en", max_chars=250):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Using device: {self.device}")
        self.tts_model = TTS("tts_models/multilingual/multi-dataset/xtts_v2").to(self.device)
        self.language = language
        self.max_chars = max_chars
        self.speaker_embeddings = {}


    def generate_speech(self, text, speaker_name):
        # Split text into chunks if it exceeds max_chars
        text_chunks = [text[i:i+self.max_chars] for i in range(0, len(text), self.max_chars)]
        
        wavs = []
        for chunk in text_chunks:
            wav = self.tts_model.tts(text=chunk,
                                     speaker=speaker_name,
                                     language=self.language,
                                     split_sentences=True)
            wavs.append(wav)

        return self.concatenate_wavs(wavs)

    @staticmethod
    def concatenate_wavs(wavs):
        return np.concatenate(wavs, axis=0)

    def batch_generate_speech(self, input_texts):
        return [self.generate_speech(text, speaker_name) for text, speaker_name in input_texts]