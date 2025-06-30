import requests as re
import json

class Chat:
    model = "llama3.1:8b" # <!-- CHANGE THE MODEL HERE --!>

    def __init__(self):
        print('Initializing...')
        self.history = []
    
    def sendChat(self, prompt: str):
        self.history.append({"role": "user", "content": prompt})

        response = re.post("http://localhost:11434/api/chat", json={
            "model": self.model,
            "messages": self.history,
            "stream": False
        }).json()
        
        reply = response["message"]["content"]

        self.history.append({"role": "assistant", "content": reply})

        return reply

    def clearChat(self):
        self.history = []

def main():
    test = Chat()
    print(test.sendChat("Hello there!"))
    print(test.sendChat("The secret word is: Bubbles."))
    print(test.sendChat("What is the secret word?"))
    test.clearChat()
    print(test.sendChat("What is the secret word?"))

if __name__ == '__main__':
    main()