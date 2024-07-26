import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


API_KEY = os.getenv('API_KEY')

# Initialize OpenAI client with your API key
client = OpenAI(api_key=API_KEY)

# Streamlit app title
st.title('Chatbot Response Testing:pencil:')

# Prompt input field
prompt = st.text_area('Enter your qustions here:', '')

# Generate button
if st.button('Generate Response'):
    # Make a request to generate the letter of appreciation
    response = client.chat.completions.create(
       
        model ="ft:gpt-3.5-turbo-0125:cache-labs-llc:vipsupportbot:9pA8cGEl",
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Answer the user's questions accurately based on the provided data."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.7,
        max_tokens=300
    )

    # Extract the content of the generated letter
    letter_content = response.choices[0].message.content

    # Display the generated letter
    st.subheader('Generated chat')
    st.write(letter_content)