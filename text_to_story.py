
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

MODEL = "openai/gpt-oss-120b"


def get_client():
    api_key = os.getenv("GROQ_TOKEN")

    if not api_key:
        raise ValueError(
            "GROQ_TOKEN was not found. Check your .env file."
        )

    return Groq(api_key=api_key)


def generate_story(scenario, genre="Adventure", max_words=50):
    if not scenario or not str(scenario).strip():
        raise ValueError("The image caption is empty.")

    client = get_client()

    prompt = f"""
You are a creative children's story writer.

Image description: {scenario}
Genre: {genre}
Maximum length: approximately {max_words} words.

Write an original, engaging story for children aged 5–10.
Include a clear beginning, a small challenge, and a satisfying ending.
Use simple language, vivid descriptions, and logical events.
Stay inspired by the image description.
Make the story enjoyable when read aloud.

Return only the story, without a title or explanation.
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=1000,
        temperature=0.8
    )

    if not response.choices:
        raise ValueError("Groq returned no response choices.")

    message = response.choices[0].message
    story = message.content

    if not story or not story.strip():
        raise ValueError(
            f"Groq returned empty content. Finish reason: "
            f"{response.choices[0].finish_reason}"
        )

    return story.strip()


def translate_story(story, target_language="Hindi"):
    if not story or not story.strip():
        raise ValueError("Cannot translate an empty story.")

    client = get_client()

    prompt = f"""
Translate this children's story into {target_language}.
Preserve the meaning, emotions, character names, and story flow.
Use natural language suitable for children.
Return only the translated story.

Story:
{story}
"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=600,
        temperature=0.3
    )

    if not response.choices:
        raise ValueError("Groq returned no translation response.")

    translated = response.choices[0].message.content

    if not translated or not translated.strip():
        raise ValueError("Groq returned an empty translation.")

    return translated.strip()


if __name__ == "__main__":
    test_story = generate_story(
        "A dog sitting on green grass",
        genre="Adventure",
        max_words=50
    )

    print("Generated story:", test_story)
    print("\nHindi translation:", translate_story(test_story, "Hindi"))


