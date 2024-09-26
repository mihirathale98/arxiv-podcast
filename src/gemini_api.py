import os
import time
from google.api_core import retry
from google.api_core import exceptions
import google.generativeai as genai
from google.generativeai.types import HarmCategory, HarmBlockThreshold

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))


class GeminiAPI:
    def __init__(self, model_name="gemini-1.5-flash", max_retries=3, retry_delay=1):
        self.model = genai.GenerativeModel(model_name)
        self.max_retries = max_retries
        self.retry_delay = retry_delay

    @retry.Retry(
        predicate=retry.if_exception_type(
            exceptions.ResourceExhausted,
            exceptions.ServiceUnavailable,
            exceptions.DeadlineExceeded,
            exceptions.InternalServerError
        ),
        initial=1,
        maximum=10,
        multiplier=2
    )
    def generate_with_retry(self, input_prompt, generation_config, safety_settings):
        return self.model.generate_content(
            input_prompt,
            safety_settings=safety_settings,
            generation_config=generation_config
        )

    def generate(
        self, input_prompt, temperature=0.7, top_p=0.95, top_k=100, max_tokens=2048
    ):
        safety_settings = {
            HarmCategory.HARM_CATEGORY_HATE_SPEECH: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_HARASSMENT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: HarmBlockThreshold.BLOCK_NONE,
            HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: HarmBlockThreshold.BLOCK_NONE,
        }

        generation_config = genai.GenerationConfig(
            max_output_tokens=max_tokens,
            top_k=top_k,
            top_p=top_p,
            temperature=temperature,
        )

        for attempt in range(self.max_retries):
            try:
                response = self.generate_with_retry(
                    input_prompt, generation_config, safety_settings
                )
                return response.text
            except Exception as e:
                if attempt == self.max_retries - 1:
                    raise e
                print(f"Attempt {attempt + 1} failed. Retrying in {self.retry_delay} seconds...")
                time.sleep(self.retry_delay)

        raise Exception("Max retries exceeded")