import pyttsx3

if __name__ == '__main__':
    print("Welcome to robo speaker created by harshit Aankare")
    
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    
    #properties
    engine.setProperty('rate', 150)  # Speed of speech
    
    # Speak the welcome message
    engine.say("Welcome to robo speaker created by harshit aankaree")
    engine.runAndWait()

    while True:
        text = input("Enter what you want to speak: ")
        
        if text == "!":
            engine.say("bye bye harshit")
            engine.runAndWait()
            break
        # Speak the input text
        engine.say(text)
        engine.runAndWait()