import azure.cognitiveservices.speech as speechsdk
import time

speech_config = speechsdk.SpeechConfig(subscription="e20a5fd269274049898326815aaf64b9", region="eastus")
speech_config.speech_recognition_language="de-DE"
audio_config = speechsdk.audio.AudioConfig(filename="/Users/michael/Downloads/dw548.wav")
speech_recognizer = speechsdk.SpeechRecognizer(speech_config=speech_config, audio_config=audio_config)

done = False

def stop_cb(evt):
    print('CLOSING on {}'.format(evt))
    speech_recognizer.stop_continuous_recognition()
    global done
    done = True

transcript = []

speech_recognizer.recognizing.connect(lambda evt: print('RECOGNIZING: {}'.format(evt.result.text)))
speech_recognizer.recognized.connect(lambda evt: transcript.append(format(evt.result.text)))
speech_recognizer.session_started.connect(lambda evt: print('SESSION STARTED: {}'.format(evt)))
speech_recognizer.session_stopped.connect(lambda evt: print('SESSION STOPPED {}'.format(evt)))
speech_recognizer.canceled.connect(lambda evt: print('CANCELED {}'.format(evt)))

speech_recognizer.session_stopped.connect(stop_cb)
speech_recognizer.canceled.connect(stop_cb)

speech_recognizer.start_continuous_recognition()
while not done:
    time.sleep(.5)

transcript = ' '.join(transcript)
print(transcript)
