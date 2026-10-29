from google import genai
import os
import datetime
import json
# client = genai.Client()
# for m in client.models.list():
#     print(m.name)

class Assistant:
    def __init__(self, json_file):
        print("Welcome, enter quit to exit")
        self.client = genai.Client()
        self.history = []
        self.json_file = json_file

    def start(self):
        if os.path.exists(self.json_file) and os.path.getsize(self.json_file) != 0: 
            with open("AI_history.json", mode = "r", encoding = "UTF-8") as f:
                self.history = json.load(f)

        while True:
            user_input = input("Enter prompt: ")
            if user_input.lower() != "quit":
                self.history.append({"role": "user", "parts": [{"text": user_input}], "time": datetime.datetime.now().isoformat()})
                self.AI_magic()

            else:
                break
                
    def AI_magic(self):
        self.history_no_time = []
        for line in self.history:
            self.history_no_time.append({"role": line["role"], "parts": line["parts"]})
        response = self.client.models.generate_content(model = "gemini-3.5-flash-lite", contents = self.history_no_time)
        reply_text = response.text
        print(reply_text)
        self.history.append({"role": "model", "parts": [{"text": reply_text}], "time": datetime.datetime.now().isoformat()})
        with open(self.json_file, mode = "w", encoding = "UTF-8") as f:
            json.dump(self.history, f)

if __name__ == "__main__":
    assistant = Assistant("AI_history.json")
    assistant.start()