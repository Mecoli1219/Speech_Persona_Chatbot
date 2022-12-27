# Setup
## for speech-to-text
import speech_recognition as sr

## for text-to-speech
from gtts import gTTS

## for data
import os

from persona_chatbot import chat as persona_chat
from persona_chatbot import personality_str

# Build the AI
class ChatBot():
     def __init__(self, name):
          print("--- starting up", name, "---")
          self.name = name
          self.text = ""
          self.history = []
          self.chat = ""

     def speech_to_text(self):
          recognizer = sr.Recognizer()
          self.text = ""
          while self.text == "":
               with sr.Microphone() as mic:
                    recognizer.adjust_for_ambient_noise(mic)
                    print("listening...", end="\r")
                    audio = recognizer.listen(mic)
               try:
                    print("Thinking... ", end="\r")
                    self.text = recognizer.recognize_google(audio)
                    print("me --> ", self.text)
               except:
                    pass

     @staticmethod
     def text_to_speech(text):
          print("ai --> ", text)
          speaker = gTTS(text=text, lang="en", slow=False)
          try:
               os.remove("res.mp3")
          except:
               pass
          speaker.save("res.mp3")
          os.system("start res.mp3")  #mac->afplay | windows->start



# Run the AI
if __name__ == "__main__":
    
     ai = ChatBot(name="mecoli")
     os.environ["TOKENIZERS_PARALLELISM"] = "true"

     print("Personality: ", personality_str)

     res = "hello, here is my persona." + personality_str
     ai.text_to_speech(res)

     end = False
     debug = False
     while not end:
          if debug:
               ai.text = input(">>>")
          else:
               ai.speech_to_text()
          if any(i in ai.text.lower() for i in ["bye"]):
               end = True
          ## conversation
          success = False
          while not success:
               try:
                    chat, ai.history, ai.chat = persona_chat(ai.text, ai.history)
                    res = str(chat).strip()
                    ai.text_to_speech(res)
                    success = True
               except:
                    pass