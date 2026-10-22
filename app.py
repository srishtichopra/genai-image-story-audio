
import streamlit as st
from image_to_text import generate_caption
from text_to_story import generate_story, translate_story
from text_to_speech import generate_audio

st.set_page_config(page_title="Image to Story to Audio")
st.title("Turn an Image into a Narrated Story")

# User controls
col1, col2 = st.columns(2)

with col1:
    genre = st.selectbox(
        "Story genre",
        ["Adventure", "Comedy", "Horror", "Romantic", "Mystery"]
    )

with col2:
    max_words = st.slider(
        "Story length (words)",
        min_value=30,
        max_value=150,
        value=50,
        step=10
    )

language_choice = st.radio(
    "Audio language",
    ["English", "Hindi"]
)

lang_code = "hi" if language_choice == "Hindi" else "en"

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["jpg", "jpeg", "png"]
)

if uploaded_file is not None:

    try:
        with open("uploaded_image.png", "wb") as f:
            f.write(uploaded_file.getbuffer())
        with st.spinner("Processing image..."):
            caption = generate_caption(uploaded_file)

        if not caption or not str(caption).strip():
            st.error("Could not generate an image caption. Please try another image.")
            st.stop()

        st.image(
            uploaded_file,
            caption="Uploaded Image",
            use_container_width=True
        )

        st.subheader("Image Scenario")
        st.write(caption)

        with st.spinner("Writing your story..."):
            story = generate_story(
                str(caption),
                genre=genre,
                max_words=max_words
            )

        if not story or not str(story).strip():
            st.error(
                "Story generation returned empty text. "
                "Please check your Groq API key and model."
            )
            st.stop()

        story = str(story).strip()

        st.subheader(f"Your Story ({genre})")
        st.write(story)

        final_text = story

        if lang_code == "hi":
            with st.spinner("Translating story into Hindi..."):
                final_text = translate_story(story, "Hindi")

            if not final_text or not str(final_text).strip():
                st.error(
                    "Hindi translation returned empty text. "
                    "Please try again."
                )
                st.stop()

            final_text = str(final_text).strip()

            st.subheader("Hindi Translation")
            st.write(final_text)

        st.caption(f"Story length: {len(final_text.split())} words")

        with st.spinner("Generating audio narration..."):
            audio_path = generate_audio(
                final_text,
                language=lang_code
            )

        st.subheader("Narrated Audio")
        st.audio(audio_path)

        with open(audio_path, "rb") as audio_file:
            st.download_button(
                label="Download Audio",
                data=audio_file,
                file_name=f"story_audio_{lang_code}.mp3",
                mime="audio/mpeg"
            )

    except Exception as e:
        st.error(f"Something went wrong: {e}")
