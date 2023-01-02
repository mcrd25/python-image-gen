import os
import openai
from pprintpp import pprint as pp
import pandas as pd

# openai.organization = ""
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = ".api_key"
TEXT_MODEL = "ada"
INITIAL_PROMPT = "write a story about a cat"

res = openai.Completion.create(
        model=TEXT_MODEL,
        prompt=INITIAL_PROMPT
prompt = res["choices"][0]["text"]
