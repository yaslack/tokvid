from quart import Quart, render_template, websocket,redirect,request,url_for,session
import os,time,asyncio
from requests_html import AsyncHTMLSession

app = Quart(__name__)

path="static/url/"

async def dynamic_page(url):
    try:
        session = AsyncHTMLSession()
        r = await session.get(url)
        await r.html.arender()  # this call executes the js in the page
        data = r.text.encode().decode('unicode-escape')
        element = data.split('"preloadList":[{"url":"',1)[1]
        video_url = element.split('","',1)[0]
        desc = element.split('"desc":"',1)[1].split('","',1)[0]
        cover = element.split('"cover":"',1)[1].split('","',1)[0]
        await session.close()
        return (video_url,desc,cover)
    except BaseException as err:
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
def internal_error(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(404)
def internal_error(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(429)
def internal_error(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(500)
def internal_error(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(502)
def internal_error(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(503)
def internal_error(error):
    return redirect(url_for('errorPage'))

@app.errorhandler(504)
def internal_error(error):
    return redirect(url_for('errorPage'))


if __name__ == '__main__':
   app.run()
