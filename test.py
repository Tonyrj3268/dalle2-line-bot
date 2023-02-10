import dalle2
prompt='a cute shark is playing soccer on the beach'
da = dalle2.dalle2()
img_url =da.produce_img(prompt)
print(img_url)