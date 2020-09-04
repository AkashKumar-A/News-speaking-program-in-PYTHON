import requests
import json
import time
import pyttsx3
"""You need to install this module"""
voiceEngine=pyttsx3.init()
def speak(str):
    voiceEngine.setProperty('rate', 130)
    voiceEngine.say(str)
    voiceEngine.runAndWait()
if __name__=='__main__':
    speak("News for today.. ")
    try:
        url = "https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=d093053d72bc40248998159804e0e67d"
        news = requests.get(url).text
        news_dict = json.loads(news)
        arts = news_dict['articles']
        for article in arts:
            print(article['title'])
            speak(article['title'])
            speak("Next news is....")
    except Exception as e:
        speak("Sorry,sir I not connected to the internet at this moment")