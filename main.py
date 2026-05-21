import speech_recognition as sr

recognizer = sr.Recognizer()

audio_file = "sample.wav"

with sr.AudioFile(audio_file) as source:
    print("Listening to audio...")

    audio_data = recognizer.record(source)

    try:
        text = recognizer.recognize_google(audio_data)

        print("\nTranscribed Text:")
        print(text)

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Error:", e)