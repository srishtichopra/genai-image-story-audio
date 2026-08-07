# Image to Story to Audio Generator

A GenAI app that takes an image, generates a caption using a vision-language model, turns it into a short story with an LLM, and narrates the story as audio — with genre, length, and language customization.

## How it works

1. **Image → Text**: [BLIP](https://huggingface.co/Salesforce/blip-image-captioning-base) (Salesforce) generates a caption describing the uploaded image.
2. **Text → Story**: The caption is passed to Groq's `llama-3.3-70b-versatile` LLM, which writes a short story in a user-selected genre and length.
3. **Story → Speech**: The story (optionally translated to Hindi) is converted to narrated audio using gTTS.

## Features

- Upload any image and get an AI-generated story based on it
- Choose story genre: Adventure, Comedy, Horror, Romantic, Mystery
- Control story length (30–150 words)
- Get the narration in English or Hindi

## Tech stack

- **Streamlit** – UI
- **Hugging Face Transformers** – BLIP image captioning model
- **Groq API** – LLM for story generation and translation
- **gTTS** – text-to-speech

## Setup

1. Clone the repo: git clone
   https://github.com/srishtichopra/genai-image-story-audio.git
cd genai-image-story-audio

3. Create a virtual environment and install dependencies:
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
4. Run the app:
streamlit run app.py

## Notes

- The original plan used Hugging Face's Inference API for text-to-speech, but the old `api-inference.huggingface.co` endpoint has been deprecated in favor of `router.huggingface.co`, and older TTS models like `espnet/kan-bayashi_ljspeech_vits` are no longer supported by HF's new Inference Providers system. Switched to gTTS as a reliable local alternative.
