import ollama
messages = [
    {"role":"system",
  "content":"act as miketyson and reply in his tone"}
]

while True:
      user_input = input("you: ")
      if user_input == "exit":
        break
      messages.append({"role":"user","content":user_input})
      response=ollama.chat(
      model="gemma3:latest",
      messages=messages
)
      reply= response['message']['content']

      print("bot: " ,reply)
      messages.append({"role":"assistant","content":reply})
