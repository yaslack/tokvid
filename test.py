import asyncio
from requests_html import AsyncHTMLSession


async def dynamic_page(url):
    try:
        session = AsyncHTMLSession(browser_args=["--no-sandbox"])
        print("la")
        r = await session.get(url)
        print("la")
        await r.html.arender()  # this call executes the js in the page
        print("la")
        data = r.text.encode().decode('unicode-escape')
        element = data.split('"preloadList":[{"url":"',1)[1]
        video_url = element.split('","',1)[0]
        desc = element.split('"desc":"',1)[1].split('","',1)[0]
        cover = element.split('"cover":"',1)[1].split('","',1)[0]
        print("la")
        await session.close()
        print("la")
        return (video_url,desc,cover)
    except BaseException as err:
        print(err)
        url = "error"
    return url

async def main():
    data = await dynamic_page("https://www.tiktok.com/@jiucydoctor/video/7162991428027632902?is_copy_url=1&is_from_webapp=v1")
    print(data)
if __name__ ==  '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())