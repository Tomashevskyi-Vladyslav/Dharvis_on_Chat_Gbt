from gtts import gTTS
import openai
import os

openai.api_key = "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"
os.system("taskkill /f /im wmplayer.exe")
n = 'Напиши рандомное число от 1 до 10'
model_engine = "text-davinci-003"   
setRecvest = 0
subWmp = 0

while True:
    subWmp+=1
    setRecvest+=1
    if setRecvest == 1:
        prompt = n
        completion = openai.Completion.create(engine = model_engine,prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
        response = completion.choices[0].text

        if len(response)>0:
            tts = gTTS(text='Conection in set', lang='en')
            tts.save(f"good_{subWmp}.mp3")
            os.system(f"good_{subWmp}.mp3")

        else :
            tts = gTTS(text='appiar the eror', lang='en')
            tts.save(f"good_{subWmp}.mp3")
            os.system(f"good_{subWmp}.mp3")

    else :
        prompt = str(input("\nGet Request : "))
        completion = openai.Completion.create(engine = model_engine,prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.5)
        response = completion.choices[0].text
        tts = gTTS(text=response, lang='en')
        tts.save(f"good_{subWmp}.mp3")
        os.system(f"good_{subWmp}.mp3")
