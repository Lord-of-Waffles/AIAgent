import os
import sys
import argparse
from dotenv import load_dotenv
from google import genai
from google.genai import types

# load .env and get API key
load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

# connect to API and send prompt
client = genai.Client(api_key=api_key)

parser = argparse.ArgumentParser()  
parser.add_argument("--verbose", action="store_true")
parser.add_argument("prompt")
args = parser.parse_args()
prompt = args.prompt
if prompt == "":
    sys.exit(1)

# this is where conversation will be stored so AI agent has context
content = types.Content(role="user", parts=[types.Part(text=prompt)])
messages = []
messages.append(content)
response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)

if args.verbose:
    print(f"User prompt: {prompt}")
    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
else:
    print(response.text)    
    #  print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    # print(f"Response tokens: {response.usage_metadata.candidates_token_count}")