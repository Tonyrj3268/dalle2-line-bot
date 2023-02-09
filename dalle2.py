import os
import openai
openai.organization = "org-tHt70UMGlNYxmVgdarPogPhh"
openai.api_key = "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"
#openai.Model.list()
from google.colab.patches import cv2_imshow
import cv2
import base64
import numpy as np
def json_to_img(json, download=False, name='some_image.png'):
  imgdata = base64.b64decode(json)
  img = cv2.imdecode(np.frombuffer(imgdata, np.uint8), cv2.IMREAD_COLOR)
  img = cv2.resize(img, (150, 150))
  cv2_imshow(img)
  if download:
    filename = name  # I assume you have a way of picking unique filenames
    with open(filename, 'wb') as f:
        f.write(imgdata)

response = openai.Image.create(
  prompt="a blue shark eating ice-cream",
  n=1,
  size="1024x1024",
  response_format='b64_json'
)
json = response['data'][0]['b64_json']
#image_url = response['data'][0]['url'] 
#url will expire
json_to_img(json, download=True, name="shark_eat_icecream.png")