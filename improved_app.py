
import streamlit as st
from pytube import YouTube

def download_video(url, download_path):
    try:
        st.info("Downloading... Please wait.")
        yt = YouTube(url)
        video = yt.streams.filter(file_extension="mp4", progressive=True).first()
        video.download(download_path)
        st.success("Download complete!")
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")

def main():
    st.title("YouTube Downloader App")
    st.write("Enter the YouTube video URL and choose a download path.")

    # Input fields
    video_url = st.text_input("Enter YouTube Video URL:", "")
    download_path = st.text_input("Enter Download Path:", "./downloads")

    # Download button
    if st.button("Download Video"):
        if not video_url or not download_path:
            st.warning("Please enter both a video URL and a download path.")
        else:
            download_video(video_url, download_path)

if __name__ == "__main__":
    main()
