from hmac import trans_5C
import streamlit as st
import whisper

st.title("Whisper App")

st.write("This is a simple app to demonstrate how to use Streamlit")

audio_file = st.file_uploader("Upload your audio file", type=["mp3", "wav", "ogg","m4a"])


model = whisper.load_model("base")
st.text("Model Loaded")


# def get_audio_file_content(file):
#     fine_details = {"filename":file.name, "filetype":file.type, "filesize":file.size}   
#     return fine_details


# if st.sidebar.button("Load Model"):
#     model = load_whisper_model()
#     st.sidebar.success("Model Loaded")

if st.sidebar.button("transcribe audio"):
    if audio_file is not None:
        st.sidebar.success("Transcribing...")
        # file = get_audio_file_content(audio_file)
        # st.audio(audio_file, format="audio/wav")
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success("Transcription complete")
        # st.text(transcription["text"])
        st.markdown(transcription["text"])

    else:
        st.sidebar.error("Upload an audio file first")


st.sidebar.header("play original audio file")
st.sidebar.audio(audio_file)