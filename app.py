import streamlit as st
from image_to_text import generate_caption
from text_to_story import generate_story, translate_story
from text_to_speech import generate_audio

st.set_page_config(page_title="Image to Story to Audio")
st.title("Turn an Image into a Narrated Story")

# --- User controls ---
col1, col2 = st.columns(2)
with col1:
    genre = st.selectbox("Story genre", ["Adventure", "Comedy", "Horror", "Romantic", "Mystery"])
with col2:
    max_words = st.slider("Story length (words)", min_value=30, max_value=150, value=50, step=10)

language_choice = st.radio("Audio language", ["English", "Hindi"])
lang_code = "hi" if language_choice == "Hindi" else "en"

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    with open("uploaded_image.png", "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Generating caption..."):
        caption = generate_caption("uploaded_image.png")
    st.subheader("Scenario")
    st.write(caption)

    with st.spinner("Writing story..."):
        story = generate_story(caption, genre=genre, max_words=max_words)
    st.subheader(f"Story ({genre})")
    st.write(story)

    final_text = story
    if lang_code == "hi":
        with st.spinner("Translating to Hindi..."):
            final_text = translate_story(story, "Hindi")
        st.subheader("Hindi Translation")
        st.write(final_text)

    with st.spinner("Generating audio..."):
        audio_path = generate_audio(final_text, language=lang_code)
    st.subheader("Narrated Audio")
    st.audio(audio_path)