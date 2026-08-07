
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

def generate_story(scenario, genre="Adventure", max_words=50):
    client = Groq(api_key=os.getenv("GROQ_TOKEN"))
    
    prompt = f"You are a creative storyteller. Write a short story, max 100 words, based on this scenario: {scenario}"
    
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )
    
    story = response.choices[0].message.content
    return story

def translate_story(story, target_language="Hindi"):
    client = Groq(api_key=os.getenv("GROQ_TOKEN"))

    prompt = f"Translate this story into {target_language}. Only return the translated text, nothing else:\n\n{story}"

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content


if __name__ == "__main__":
    test_scenario = "a dog sitting on grass"
    test_story = generate_story(test_scenario)
    print("Generated story:", test_story)

    translated = translate_story(test_story, "Hindi")
    print("Translated story:", translated)
