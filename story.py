import asyncio
from secret_manager import SecretManager
import openai
from pprintpp import pprint as pp
import pandas as pd

secret_manager = SecretManager()
lock = asyncio.Lock()

secrets = secret_manager.get_secrets("openai")
assert "openai" in secret_manager.get_services()
openai.api_key = secrets["api_key"]
# openai.api_key_path = ".api_key"
# openai.organization = secrets["org_key"]
# openai.organization = ".org_key"
async def story_gen():
    # Set up the prompt
    story_prompt = ""

    # Set the model to use and the number of completions
    model_engine = "text-davinci-002"
    num_completions = 1
    max_tokens = 110
    story_iterations = 5
    story = "Once upon a time, there was a cat that loved coffee."
    story_prompt = "His name was..."
    image_size = "512x512"
    column_names=["Prompt",'Image URL']
    file_name = "story_images.csv"
    prompt = ""


    for i in range(story_iterations):
        print(i + 1)

        if i == story_iterations - 1:
            story_prompt = "End the story: " + completions.choices[0].text
        elif i != 0:
            story_prompt = "Continue the story: " + completions.choices[0].text
        else:
            story_prompt = "Continue the story: " + story + " " + story_prompt
        print("\n prompt: \n"+ story_prompt)
        async with lock:
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=story_prompt,
                max_tokens=max_tokens,
                n=num_completions,
                temperature=0.5,
            )


        story += completions.choices[0].text
        print("\n story so far: \n")
        pp(story)
        if (i == 0):
            prompt = story.strip()
        else:
            prompt = completions.choices[0].text.strip()
        print("\n image prompt: \n")
        print(prompt)
        async with lock:
            response = openai.Image.create(
                prompt=prompt,
                n=1,
                size=image_size
            )
        image_url = response['data'][0]['url']
        row = [[prompt, image_url]]
        if (i == 0):
            df = pd.DataFrame(row, columns=column_names)
        else:
            df.loc[len(df)] = [prompt, image_url]

    print("\n\nThe complete story: \n" + story)

    df.to_csv(file_name, index=False)
async def main():
    await story_gen()

asyncio.run(main())
