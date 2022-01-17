import pyaudio
import wave
import requests
import logging
logger = logging.getLogger(__name__)

__subscription_key = ''
__region = 'uksouth'

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 16000

def record(filename: str, duration=5.0) -> bool:
    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT, channels=CHANNELS, rate=RATE,
                    input=True, frames_per_buffer=CHUNK)

    logger.info("recording for %s seconds", duration)

    frames = []

    for i in range(0, int(RATE / CHUNK * duration)):
        data = stream.read(CHUNK)
        frames.append(data)

    logger.info("done recording.")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(filename, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()
    return True


def speech_to_text(sound_as_binary):
    """Sends the API request to convert speech to text.
    It expects sound as a wav file and returns the response object, which contains the text in:
    response["content"]["DisplayText"].
    See also response["content"]["RecognitionStatus"] for confirmation that it worked."""
    url = f'https://{__region}.stt.speech.microsoft.com/speech/recognition/conversation/cognitiveservices/v1'
    params = {"language": "en-GB"}
    headers = {
        "Content-Type": "audio/wav",
        "Accept": "application/json",
        "Ocp-Apim-Subscription-Key" :__subscription_key
    }
    response = requests.post(url, params=params, headers=headers, data=sound_as_binary)
    return response
