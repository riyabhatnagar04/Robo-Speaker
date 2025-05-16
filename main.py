import pyttsx3

if __name__ == '__main__':
    print("Welcome to Rivo- Your personal Robo Speaker, Created by Riya")
    engine = pyttsx3.init()

    # Get available voices
    voices = engine.getProperty('voices')

    # Find a female voice and set it
    for voice in voices:
        if "female" in voice.name.lower() or "zira" in voice.id.lower():  # 'Zira' is a common female voice on Windows
            engine.setProperty('voice', voice.id)
            break

    # Intro Spoken Message
    intro_message = "Hello! I am Rivo, Your personal Robo Speaker. What would you like me to say today?"
    engine.say(intro_message)
    engine.runAndWait()

    # responses/questions for small talk
    responses = {
        "what's your name": "My name is Rivo, your personal Robo Speaker!",
        "how are you": "I'm feeling electric and ready to talk!",
        "who made you": "I was created by Riya, my amazing developer.",
        "thank you": "You're most welcome!",
        "i love you": "Aww! I love talking to you too!",
        "what can you do": "I can speak anything you type, and I'm learning more every day!",
        "what's the weather today": "I don't know, but I hope it's sunny!"
    }

    while True:
        x = input("Enter what you want me to speak: ")
        if x.lower() == "q":
            engine.say('bye bye friend')
            engine.runAndWait()
            break

        elif x in responses:
            engine.say(responses[x])

        else:
            engine.say(x)

        engine.runAndWait()



