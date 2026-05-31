"""
Task 6: Web deployment of the application using Flask.
This module defines the Flask application routes for emotion detection.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

# Initialize the Flask application
app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def emotion_detector_route():
    """
    Handle GET requests to analyze the emotion of the provided text.
    
    Returns:
        str: A formatted response with emotion scores or an error message.
    """
    # Retrieve the text to analyze from the request URL arguments (?textToAnalyze=...)
    text_to_analyze = request.args.get("textToAnalyze")

    # Pass the text to the emotion_detector function and store the response
    result = emotion_detector(text_to_analyze)
    # Handle error cases where the text is blank or invalid
    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again."

    # Build a clean, formatted string of all the emotion scores
    emotions_str = (
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']}, "
        f"'sadness': {result['sadness']}"
    )

    # Return the final analysis result to the web interface
    return (
        f"For the given statement, the system response is {emotions_str}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )

@app.route("/")
def render_index_page():
    """
    Initiate the rendering of the main application page.
    
    Returns:
        html: The rendered index.html template.
    """
    return render_template("index.html")

if __name__ == "__main__":
    # Execute the flask app and deploy it locally on port 5000
    app.run(host="0.0.0.0", port=5000)
