import openai
import configparser
class chatgpt:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read('config.ini')
        openai.organization = config.get('open-ai', 'organization')
        openai.api_key = config.get('open-ai', 'api_key')

    def translate(self,prompt):
        prompt = "請幫我翻譯以下文本成中文 " + prompt
        response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5
        )
        
        text = response.choices[0].text.split("\n\n")[1]
        return text