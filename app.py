from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
from openai import openai
import configparser
app = Flask(__name__)

config = configparser.ConfigParser()
config.read('config.ini')
line_bot_api = LineBotApi(config.get('line-bot', 'channel_access_token'))
handler = WebhookHandler(config.get('line-bot', 'channel_secret'))

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)
        
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text:
        prompt=event.message.text
        openai = openai()
        if prompt[:2]=="翻譯":
            text = openai.translate(prompt[3:].replace("\n"," "))
            line_bot_api.reply_message(event.reply_token,[
                TextSendMessage(text = text)])
        else:
            img_url = openai.produce_img(prompt)
            line_bot_api.reply_message(event.reply_token,[
                ImageSendMessage(
                    original_content_url=img_url,
                    preview_image_url="loading.jpg"),
                TextSendMessage(text= prompt)])

if __name__ == "__main__":
    app.run()




  