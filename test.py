from TikTokApi import TikTokApi

with TikTokApi() as api:
    video = api.video(id="7158526081312640262")

    # Bytes of the TikTok video
    video_data = video.bytes()

    with open("out.mp4", "wb") as out_file:
        out_file.write(video_data)