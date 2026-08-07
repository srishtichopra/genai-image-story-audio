
from gtts import gTTS

def generate_audio(text, language="en"):
    tts = gTTS(text=text, lang=language)
    filename = f"story_audio_{language}.mp3"
    tts.save(filename)
    return filename

if __name__ == "__main__":
    test_story = "The little dog ran happily through the green grass, chasing butterflies under the warm sun."
    result = generate_audio(test_story)
    print("Audio saved at:", result)