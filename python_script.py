import requests
import openai
import os


api_endpoint = 'https://api.openai.com/v1/completions'
openai_key= os.getenv("OPENAI_KEY")