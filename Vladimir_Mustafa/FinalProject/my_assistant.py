#імпорт бібліотек
import speech_recognition as sr
import pyttsx3
import time
import openai
import os
import subprocess
import webbrowser



#Ключ API OpenAI

openai.api_key='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'
#Ініціалізація повідомлень
messages=[
    {"role":"system",
     "content":"You are a intelligent assistant."
     }
]
#Ініціалізація перетворення тексту на мовлення
engine = pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[3].id)

#функція музики
def play_music():
    music_path = "\music//Goro - Дорогу Молодым (1).mp3"

    if os.path.exists(music_path):
        os.startfile(music_path)
        engine.say("Воспроизводится музыка.")
    else:
        engine.say("Музыкальный файл не найден.")

    engine.runAndWait()

#Функція зворотного визова
def callback(recognizer,audio):
    try:
        voice=recognizer.recognize_google(audio,language="ru-RU").lower()
        print("Распознано: "+voice)
        messages.append(
            {"role":"user","content":voice},
        )
        chat=openai.ChatCompletion.create(
            model="gpt-3.5-turbo",messages=messages
        )
        reply=chat.choices[0].message.content
        if "время" in voice or "сколько времени" in voice or "текущее время" in voice:
            current_time = time.strftime("%H:%M:%S")
            reply = f"Сейчас {current_time}."
        elif "дата" in voice or "какая сегодня дата" in voice or "текущая дата" in voice:
            current_date = time.strftime("%d-%m-%Y")
            reply = f"Сегодня {current_date}."
        elif 'как тебя зовут' in voice or 'твоё имя' in voice:
            reply = 'Меня зовут Винчестер, я ваш раб'
        elif 'кто я' in voice or 'как меня зовут' in voice:
            reply = 'Вы мой повелитель, Владимир Владимирович, я готов кланится вам каждую минуту'

        elif 'иди спать' in voice or 'пока' in voice or 'свободен' in voice or 'все отдыхай' in voice or 'стоп' in voice:
            exit()
        elif "музыка" in voice or "включи музыку" in voice:
            play_music()
            return True
        elif "steam" in voice or "открой steam" in voice:
            try:
                subprocess.run("C:\Steam\\Steam.exe", check=True)
                return True
            except subprocess.CalledProcessError:
                engine.say("Не удалось открыть Steam.")
        elif "youtube" in voice or "открой youtube" in voice:
            webbrowser.open("https://www.youtube.com/")
            return True





        else:
            chat = openai.ChatCompletion.create(
                model="gpt-3.5-turbo", messages=messages
            )
            reply = chat.choices[0].message.content
        print(f"Винчестер: {reply}")
        engine.say(reply)
        engine.runAndWait()
    except sr.UnknownValueError:
        print('Голос не распознан')
    except sr.RequestError:
        print('Неизвестная ошибка!')

#захоплення звуку з мікрофону
def record_sound():

    r=sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        r.adjust_for_ambient_noise(source)
        audio=r.listen(source)
        callback(r,audio)

#привітання
engine.say("Приветствую мой повелитель , могу ли я вам помочь?")
engine.runAndWait()

#Основной цикл
while True:
    record_sound()
