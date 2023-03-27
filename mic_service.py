import speech_recognition as sr

class AudioListeningError(Exception):
    pass

class MicService:

    def listen_audio(self):
        microfone = sr.Recognizer()

        with sr.Microphone() as source:
            microfone.adjust_for_ambient_noise(source)
            print("Listening...")
            audio = microfone.listen(source)

        try:
            frase = microfone.recognize_google(audio, language='pt-BR')
            print(frase)
            return frase

        except sr.UnknownValueError:
            raise AudioListeningError("O serviço de reconhecimento de fala não entendeu o que foi dito.")

        except sr.RequestError:
            raise AudioListeningError("Não foi possível se conectar ao serviço de reconhecimento de fala.")
