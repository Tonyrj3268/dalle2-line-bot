from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import *
import json
import random
from dalle2 import dalle2
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('BdimudProf4VkCVmh0C2jAIz1Q+gHGGjehIDN/aENEHbaER8RW2Lwof7bKDCBRVbi0qTmsTTfz5hZUjaGd/RpKbHJAffiO4NdnnEGINAUbdkVWT67s9ZE5iH6DUzypno/IPqWfZq1nx2zVBeLndLZwdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('5b4a7c9c7d6fc61bc1461e1669ae4c87')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']

    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    
    try:
        print(body, signature)
        handler.handle(body, signature)
        
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    if event.message.text:
        prompt=event.message.text
        da = dalle2.dalle2()
        img_url = da.produce_img(prompt)
        print(img_url)
        line_bot_api.reply_message(event.reply_token,[
            ImageSendMessage(
                original_content_url=img_url,
                preview_image_url='https://github.com/Tonyrj3268/temple-test/blob/main/%E8%BE%B2%E6%B0%91%E6%9B%86.png?raw=true'),
            TextSendMessage(text= prompt)])
        

if __name__ == "__main__":
    app.run()




  