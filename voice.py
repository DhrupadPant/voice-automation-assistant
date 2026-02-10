import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
print(f"Total voices found: {len(voices)}")
for i, voice in enumerate(voices):
    print(f"Voice {i}: {voice.name} - ID: {voice.id}")