import boto3
import time

aws_access_key = ""
aws_secret_key = ""

bucket_name = "masterarbeit-audio"
object_name = "1976-SekretaerinnenTreffenSchweiz.wav"

transcribeKey = str(int(time.time()))+"_"+object_name

client = boto3.client('transcribe',
	region_name="eu-central-1",
	aws_access_key_id=aws_access_key, 
    aws_secret_access_key=aws_secret_key
)

response = client.start_transcription_job(
    TranscriptionJobName=transcribeKey,
    LanguageCode='de-DE',
    MediaFormat='wav',
    Media={
        'MediaFileUri': 's3://masterarbeit-audio/'+object_name,
    },
    Settings={
        #'VocabularyName': 'string',
        #'ShowSpeakerLabels': True|False,
        #'MaxSpeakerLabels': 123,
        #'ChannelIdentification': True|False,
        #'ShowAlternatives': True|False,
        #'MaxAlternatives': 123,
        #'VocabularyFilterName': 'string',
        #'VocabularyFilterMethod': 'remove'|'mask'|'tag'
    },
    #ModelSettings={
    #    'LanguageModelName': 'string'
    #},
    #IdentifyLanguage=True|False,
    #LanguageOptions=[
    #    'af-ZA'|'ar-AE'|'ar-SA'|'cy-GB'|'da-DK'|'de-CH'|'de-DE'|'en-AB'|'en-AU'|'en-GB'|'en-IE'|'en-IN'|'en-US'|'en-WL'|'es-ES'|'es-US'|'fa-IR'|'fr-CA'|'fr-FR'|'ga-IE'|'gd-GB'|'he-IL'|'hi-IN'|'id-ID'|'it-IT'|'ja-JP'|'ko-KR'|'ms-MY'|'nl-NL'|'pt-BR'|'pt-PT'|'ru-RU'|'ta-IN'|'te-IN'|'tr-TR'|'zh-CN'|'zh-TW'|'th-TH'|'en-ZA'|'en-NZ',
    #],
    #Subtitles={
    #    'Formats': [
    #        'vtt'|'srt',
    #    ]
    #},
    #LanguageIdSettings={
    #    'string': {
    #        'VocabularyName': 'string',
    #        'VocabularyFilterName': 'string',
    #        'LanguageModelName': 'string'
    #    }
    #}
)

print(response)