import os
import openai
from pprintpp import pprint as pp
openai.organization = "org-6f9VZtwKb6sSLrPyTgGlXFGW"
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = ".api_key"
# pp(openai.Model.list())

response = openai.Image.create(
  prompt="a high quality photo of the streets of Paris",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)