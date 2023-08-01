import os
import webbrowser
import speech_recognition as sr
import pyttsx3
import openai
from config import apikey
import datetime

def say(text, rate=120):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(text)
    engine.runAndWait()

chatStr=""

def chat(prompt):
    global chatStr
    openai.api_key = apikey
    chatStr += f"User: {prompt}\nRidd:"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        say(response["choices"][0]["message"]["content"])
        chatStr += f"{response['choices'][0]['message']['content']}\n"
        print(chatStr)
    except Exception as e:
        return "Some error occurred sorry from ridd"


def ai(prompt):
    openai.api_key = apikey
    text = f'openai response for prompt: {prompt}\n***********\n\n'
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    try:
        text += response["choices"][0]["message"]["content"]
        if not os.path.exists("openai"):
            os.mkdir("openai")

        with open(f"openai/{''.join(prompt.split('AI')[1:])}.txt", "w")as f:
            f.write(text)
    except Exception as e:
        return "Some error occurred sorry from ridd"

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        try:
            query = r.recognize_google(audio, language="en-in")
            return query
        except Exception as e:
            return "Some error occurred sorry from ridd"

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')
    say("Hello I am Ridd's AI", rate=120)
    while True:
        print("Listening...")
        text = takecommand()
        sites = [["youtube", "https://youtube.com"], ["wikipedia", "https://wikipedia.com"],["chatgpt","https://chat.openai.com/"],
                 ["google", "https://google.com"], ["weird pub", "https://weirdpub.blinkstore.in"],["gmail","https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox"],]
        files=[["download","start  C:\\Users\\vridd\Downloads"],["design","C:\\Users\\vridd\OneDrive\designs"]]
        #commented this part of code as using chatgpt only to answer the question.
        #greetings=[["hello","Hii how can I help you"],["thank you","Your welcome!I hope that you got the answer"],["bye","Goodbye. Feel free to ask anything.Have a great day"]]
        # for greet in greetings:
        #     if f"{greet[0]}".lower() in text.lower():
        #         say(f"{greet[1]}")
        for site in sites:
            if f"open {site[0]}".lower() in text.lower():
                say(f"opening {site[0]} Madam")
                webbrowser.open(site[1])
        for file in files:
            if f"open {file[0]}".lower() in text.lower():
                say(f"opening {file[0]} Madam")
                os.system(f"start {file[1]}")
        if "the time" in text:
                strfTime = datetime.datetime.now().strftime("%H:%M")
                say(f"Mam the time is {strfTime}")
        elif "using AI" in text:
            ai(prompt=text)
            say("Check open ai folder for the answer")
        else:
            chat(prompt=text)

# todo:Extra things which also you can add
# you can also do the login in instagram using webdriver
# you can also play music
# you can search out the music also from directory
# if"open music" in query:
#     musicpath = write the path where the music is there
#     os.system(f"open {musicpath}")


# import win32com.client
#
# speaker = win32com.client.Dispatch("SAPI.Spvoice")
# # Press the green button in the gutter to run the script.
# while 1:
#     print("Enter word")
#     s=input()
#     speaker.Speak(s)
