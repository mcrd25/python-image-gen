import os
import openai

# openai.organization = ""
# openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_key_path = ".api_key"
# pp(openai.Model.list())

initial_prompt = "an impressionist painting"
IMAGE_SIZE = "1024x1024"

response = openai.Image.create(
  prompt=initial_prompt,
  n=1,
  size=IMAGE_SIZE
)

image_url = response['data'][0]['url']
print(image_url)
