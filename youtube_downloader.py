import streamlit as st
import yt_dlp
import os

def download_youtube_video(url, save_path="."):
    ydl_opts = {'outtmpl': os.path.join(save_path, '%(title)s.%(ext)s')}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_title = info_dict.get('title', 'video')
        return f"{video_title}.mp4"

st.title("YouTube Video Downloader")
st.write("Enter the YouTube video URL below to download the video:")

# Input for YouTube URL
video_url = st.text_input("YouTube Video URL:")

# Add helpful note for the save location
st.write("### Save Location Note:")
st.write("""
You can either type the path where you want to save the video, such as:
- `C:/Users/YourName/Downloads/`
- `./my_videos/` (relative path)
- `./` for saving in the current directory.

If the path doesn't exist, it will be created automatically.
""")

# Input for Save Path
save_path = st.text_input("Path to Save the Video:", ".")

if st.button("Download"):
    if video_url:
        try:
            st.write("Downloading...")
            video_filename = download_youtube_video(video_url, save_path)
            st.success(f"Download completed! Saved as {video_filename}")
            st.write(f"File saved at: {os.path.join(save_path, video_filename)}")
        except Exception as e:
            st.error(f"Error: {e}")
    else:
        st.warning("Please enter a valid YouTube video URL.")
