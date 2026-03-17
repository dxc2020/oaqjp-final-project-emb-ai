import requests
import json

def emotion_detector(text_to_analyze):
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    headers = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    response = requests.post(url, json = myobj, headers = headers)
    formatted_response = json.loads(response.text)
    prediction = formatted_response['emotionPredictions'][0]
    result = dict()
    result['anger'] = prediction['emotion']['anger']
    result['disgust'] = prediction['emotion']['disgust']
    result['fear'] = prediction['emotion']['fear']
    result['joy'] = prediction['emotion']['joy']
    result['sadness'] = prediction['emotion']['sadness']    
    dominant_emotion_score = 0.0
    for key, value in result.items():        
        if dominant_emotion_score < value:
            dominant_emotion_score = value
            dominant_emotion = key        
    result['dominant_emotion'] = dominant_emotion
    return result