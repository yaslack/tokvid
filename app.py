from quart import Quart, render_template, websocket,redirect,request,url_for,session
import os,time,asyncio
from requests_html import AsyncHTMLSession
from TikTokApi import TikTokApi
import nest_asyncio
nest_asyncio.apply()


app = Quart(__name__)
path="static/url/"

async def dynamic_page(url):
    try:
        print("la")
    
        api =  TikTokApi()
        print("la")

        print(url)
        data =  api.video(url=url).info()
        print("la")
        # Bytes of the TikTok video
        data=str(data)
        print("la")
        element = data.split("'UrlList': ['",1)[1]
        video_url = element.split("'",1)[0]
        element = data.split("'createTime':",1)[1]
        desc = element.split(", 'desc': ",1)[1].split(',',1)[0]
        cover = data.split("'cover': '",1)[1].split("'",1)[0]
        print("la")
        return (video_url,desc,cover)
    except BaseException as err:
        print(err)
        url = "error"
    return url

@app.route('/',methods=['GET', 'POST'])
def home():
    return redirect('/Home')

@app.route('/Home', methods=['GET', 'POST'])
async def homePage():
    if request.method == "POST":
        # getting input with name = fname in HTML form
        url = (await request.form)["url"]
        data = await dynamic_page(url)
        if data != "error":
            return redirect(url_for('downloadPage', video= data[0], desc= data[1], cover= data[2]))
        else:
            return redirect(url_for('errorPage'))
    return await render_template('home.html')

@app.route('/Download/', methods=['GET', 'POST'])
async def downloadPage():
    video=request.args.get("video")
    desc=request.args.get("desc")
    cover=request.args.get("cover")
    return await render_template('download.html',video=video, desc= desc, cover= cover)

@app.route('/Error/', methods=['GET', 'POST'])
async def errorPage():
    return await render_template('error.html')

@app.route('/Contact/', methods=['GET', 'POST'])
async def contactPage():
    return await render_template('contact.html')

@app.route('/Privacy/', methods=['GET', 'POST'])
async def privacyPage():
    return await render_template('privacy.html')

    
@app.errorhandler(400)
def internal_error(error):
    return redirect(url_for('errorPage'))
    
@app.errorhandler(403)
def internal_error1(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(404)
def internal_error2(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(429)
def internal_error3(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(500)
def internal_error4(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(502)
def internal_error5(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(503)
def internal_error6(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(504)
def internal_error7(error):
    return redirect(url_for('errorPage'))


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
