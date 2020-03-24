from google.cloud import speech_v1p1beta1
from google.cloud.speech_v1p1beta1 import enums
import io


def convert_cloud_file(storage_uri, language_code="en-US", samplerate=44100, encoding='wav'):
    """
    Performs synchronous speech recognition on an cloud audio file

    Args:
      storage_uri URI for audio file in Cloud Storage, e.g. gs://[BUCKET]/[FILE]
      langue_code to define the language of the audi file
    """

    client = speech_v1p1beta1.SpeechClient()

    # storage_uri = 'gs://cloud-samples-data/speech/brooklyn_bridge.mp3'

    # The language of the supplied audio
    # language_code = "en-US"

    # Sample rate in Hertz of the audio data sent, as we only use wav file, this is not needed
    # sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    #encoding = enums.RecognitionConfig.AudioEncoding.MP3
    # Json format that is send to the Googple Speech to Text_API
    config = {
        "language_code": language_code,

    }
    audio = {"uri": storage_uri}

    # recognize = POST to API
    response = client.recognize(config, audio)
    # The response is a Json format that needs to be parsed
    text = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        text.append(u"Transcript: {}".format(alternative.transcript))
    return text


def convert_local_file(local_file_path, language_code="en-US", samplerate=44100, encoding='wav'):
    """
    Performs synchronous speech recognition on an local audio file

    Args:
      local_file_path local location of the audio file
      langue_code to define the language of the audi file
    """

    client = speech_v1p1beta1.SpeechClient()

    # storage_uri = 'local file'

    # The language of the supplied audio
    # language_code = "en-US"

    # Sample rate in Hertz of the audio data sent, as we only use wav file, this is not needed
    # sample_rate_hertz = 44100

    # Encoding of audio data sent. This sample sets this explicitly.
    # This field is optional for FLAC and WAV audio formats.
    #encoding = enums.RecognitionConfig.AudioEncoding.MP3
    # Json format that is send to the Googple Speech to Text_API
    config = {
        "language_code": language_code,

    }
    with io.open(local_file_path, "rb") as f:
        content = f.read()
    audio = {"content": content}

    # recognize = POST to API
    response = client.recognize(config, audio)
    # The response is a Json format that needs to be parsed
    text = []
    for result in response.results:
        # First alternative is the most probable result
        alternative = result.alternatives[0]
        text.append(u"Transcript: {}".format(alternative.transcript))
    return text