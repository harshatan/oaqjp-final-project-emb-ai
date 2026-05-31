import unittest
from EmotionDetection.emotion_detection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    """Unit tests for validating the emotion_detector function."""

    def test_emotion_detection(self):
        """Test that various text inputs return the correct dominant emotion."""
        
        # Define a list of tuples containing (input_text, expected_dominant_emotion)
        test_cases = [
            ("I am glad this happened", "joy"),
            ("I am really mad about this", "anger"),
            ("I feel disgusted just hearing about this", "disgust"),
            ("I am so sad about this", "sadness"),
            ("I am really afraid that this will happen", "fear"),
        ]

        # Loop through each test case to validate the detector's output
        for text, expected_emotion in test_cases:
            # self.subTest isolates each case so one failure doesn't stop the whole loop
            with self.subTest(text=text):
                result = emotion_detector(text)
                
                # Assert that the detected dominant emotion matches what we expect
                self.assertEqual(result["dominant_emotion"], expected_emotion)


if __name__ == "__main__":
    # Execute all the test cases when the script is run directly
    unittest.main()