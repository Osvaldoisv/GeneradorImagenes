import requests
import streamlit as st

api_key = ''

def openai_request(prompt):
    headers = {'Autorization': f'Bearer {api_key}'}
    response = requests.post(
        'https://api.openai.com/vi/images/generations',
        headers=headers,
        json={
            'prompt': prompt,
            'model': 'dall-e-3',
            'size': '1024x1024',
            'quality': 'standard',
            'n': 1
        }
    )
    if response.status_code != 200:
        raise Exception(response.json)
    else:
        image_url = response.json()['data'][0]['url']
    
    return image_url
      
def download_image(url, filename):
    response = requests.get(url)
    with open(filename, 'wb') as file:
        file.write(response.content)

# configure the page
st.set_page_config(page_title="AI Image Generator", page_icon="📷", layout="centered")

# create a streamlit app
