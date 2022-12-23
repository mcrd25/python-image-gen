import os
import openai
from pprintpp import pprint as pp
import pandas as pd

openai.organization = "org-6f9VZtwKb6sSLrPyTgGlXFGW"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = ".api_key"
# pp(openai.Model.list())
NUM_IMAGE = 10
initial_prompt = "a high quality studio photo of a kitten drinking coffee"
IMAGE_SIZE = "512x512"
TEXT_MODEL = "ada"
PROMPT_FOR_TEXT = "write a description of an abstract painting"
FILE_NAME = "images.csv"

response = openai.Image.create(
  prompt=initial_prompt,
  n=1,
  size=IMAGE_SIZE
)

image_url = response['data'][0]['url']


column_names=["Prompt",'Image URL']
initial_row = [[initial_prompt, image_url]]
df = pd.DataFrame(initial_row, columns=column_names)


for x in range(NUM_IMAGE - 1):
    res = openai.Completion.create(
        model=TEXT_MODEL,
        prompt=PROMPT_FOR_TEXT
    )

    prompt = res["choices"][0]["text"]
    response = openai.Image.create(
        prompt=prompt,
        n=1,
        size=IMAGE_SIZE
    )

    image_url = response['data'][0]['url']
    df.loc[len(df)] = [prompt, image_url]


df.to_csv(FILE_NAME, index=False)
