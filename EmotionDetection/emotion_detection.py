import requests
import json

# Specifically done for Task # 2 for Final Project
def emotion_detector_Task2(text_to_analyse): 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict' # URL of the emotion predict service 
    myobj = { "raw_document": { "text": text_to_analyse } } # Create a dictionary with the text to be analyzed 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"} # Set the headers required for the API request 
    
    response = requests.post(url, json = myobj, headers=header) # Send a POST request to the API with the text and headers 
    
    return response.text # Return the response text from the API

# Specifically done for Task # 3 for Final Project
def emotion_detector(text_to_analyse): 
    # URL of the sentiment analysis service 
    url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    
    # Constructing the request payload in the expected format 
    myobj = { "raw_document": { "text": text_to_analyse } } 
    
    # Custom header specifying the model ID for the sentiment analysis service 
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    
    # specify the emotional dictionary
    emotionDictionary = {
        "anger": None,
        "disgust": None,
        "fear": None,
        "joy": None,
        "sadness": None,
        "dominant_emotion": None,
    }

    # Sending a POST request to the sentiment analysis API 
    response = requests.post(url, json = myobj, headers=header)
    
    # Parsing the JSON response from the API 
    formatted_response = json.loads(response.text)

    # Extract the required set of emotions, including anger, disgust, fear, joy and sadness, along with their scores
    resultEmotDict = emotionDictionary.copy()

    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    resultEmotDict["anger"] = emotions["anger"]
    resultEmotDict["disgust"] = emotions["disgust"]
    resultEmotDict["fear"] = emotions["fear"]
    resultEmotDict["joy"] = emotions["joy"]
    resultEmotDict["sadness"] = emotions["sadness"]

    dominant_emotion = max(emotions, key=emotions.get)
    resultEmotDict["dominant_emotion"] = dominant_emotion

    # Returning a dictionary containing sentiment analysis results    
    return resultEmotDict


    