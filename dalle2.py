import os
import openai

import cv2
import base64
import numpy as np
class dalle2:
    def __init__(self):
        openai.organization = "org-tHt70UMGlNYxmVgdarPogPhh"
        openai.api_key = "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"

    def json_to_img(json, download=False, name='some_image.png'):
        imgdata = base64.b64decode(json)
        img = cv2.imdecode(np.frombuffer(imgdata, np.uint8), cv2.IMREAD_COLOR)
        img = cv2.resize(img, (150, 150))
        if download:
            filename = name  # I assume you have a way of picking unique filenames
            with open(filename, 'wb') as f:
                f.write(imgdata)
    def produce_img(self,prompt,n=1,size="1024x1024",response_format='url'):
        
        response = openai.Image.create(
            prompt=prompt,
            n=n,
            size=size,
            response_format=response_format
            )
        url = response['data'][0]['url']
        
        #url = prompt
        return url