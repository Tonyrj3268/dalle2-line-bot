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
app = Flask(__name__)

# Channel Access Token
line_bot_api = LineBotApi('YAUo5y4kXJzhPCZzwgIpsURZ1sA/o3+cwUs+R6MAnhetZupjz66OqbP4nHpCPIG49svtg96C98qbuJqKSikCNo6poBNDASB+tzBnX0CstIdAoyJ/GP6ICb8FASUQ9Q7AUBRtIEo0R0VUUVVgh/kMBgdB04t89/1O/w1cDnyilFU=')
# Channel Secret
handler = WebhookHandler('fe3abf9906458712b249941336225c2a')

# 監聽所有來自 /callback 的 Post Request
@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']
    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

# 處理訊息
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='hi')
        )
import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)




  