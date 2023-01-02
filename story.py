from secret_manager import SecretManager
import openai
from pprintpp import pprint as pp
secret_manager = SecretManager()

secrets = secret_manager.get_secrets("openai")
assert "openai" in secret_manager.get_services()
print(secrets)


openai.api_key = secrets["api_key"]
# openai.api_key_path = ".api_key"
print(openai.api_key)

# Set up the prompt
story_prompt = "Complete the story: Once upon a time, there was a cat that loved coffee. His name was..."
pp(story_prompt)
# Set the model to use and the number of completions
model_engine = "text-davinci-002"
num_completions = 1

# Generate completions
completions = openai.Completion.create(
    engine=model_engine,
    prompt=story_prompt,
    max_tokens=1024,
    n=num_completions,
    temperature=0.5,
)
pp(completions)
# Print the completions
for completion in completions.choices:
    print(completion.text)
