import streamlit as st
import google.generativeai as genai
import os
from apikey import google_gemini_api_key, open_api_key
from openai import OpenAI

client = OpenAI(api_key=open_api_key)
genai.configure(api_key=google_gemini_api_key)

from streamlit_carousel import carousel


single_image = dict(
    title = "",
    text = "",
    interval = None,
    img = "",
)

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
)

chat_session = model.start_chat(
  history=[
  ]
)




st.set_page_config(layout="wide")

st.title("Your AI Writing Companion")

st.subheader("You can craft blog with AI")


with st.sidebar:
    st.title("Input blog content")
    st.subheader("Enter generate details")

    blog_title = st.text_input("Enter blog title")
    keyword = st.text_input("Enter keyword")
    num_words = st.slider("Select number of words", 250, 1000, 250)
    num_images = st.slider("Select number of images", 1, 5, 1)

    prompt_part = [
        f"Generate a comprehensive, engaging blog post relevant to the given title \"{blog_title}\" and keywords \"{keyword}\". The content should be in {num_words} words.",
    ]

    submit_button = st.button("Generate Blog")


if submit_button:
    #st.image("images.jpg")


    response = chat_session.send_message(prompt_part)

    images=[]

    images_gallery = []

    for i in range(num_images):
        image_response = client.images.generate(
            model = "dall-e-3",
            prompt = f"Generate a blog post iamge on the title : {blog_title}",
            size = "1024x1024",
            quality = "standard",
            n = 1
        )
        new_image = single_image.copy()
        new_image["title"] = f"Image {i + 1}"
        new_image["text"] = f"{blog_title}"
        new_image["img"] = image_response.data[0].url
        images_gallery.append(new_image)

    st.title("Blog images here")
    carousel(items=images_gallery, width=1)

    st.title("Blog Post:")
    st.write(response.text)


