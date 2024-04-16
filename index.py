import pyttsx3

# Initialize the TTS engine
engine = pyttsx3.init()

# Set properties (optional)
engine.setProperty('rate', 125)    # Speed percent (can go over 100)
engine.setProperty('volume', 0.9)  # Volume 0-1

# Change the voice to female
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # 0 for male voice, 1 for female voice

# Text to be converted to speech
text = "Hello, how are you today?"

# Convert text to speech
engine.say(text)

# Wait for speech to finish
engine.runAndWait()
