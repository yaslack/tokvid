from TikTokApi import TikTokApi

with TikTokApi() as api:
    data = api.video(url="https://www.tiktok.com/@epicwarzyt/video/7152087644430748934?is_from_webapp=v1&item_id=7152087644430748934").info()

    # Bytes of the TikTok video
    data=str(data)

    element = data.split("'UrlList': ['",1)[1]
    video_url = element.split("'",1)[0]
    element = data.split("'createTime':",1)[1]
    desc = element.split(", 'desc': ",1)[1].split(',',1)[0]
    cover = data.split("'cover': '",1)[1].split("'",1)[0]
    print(desc)