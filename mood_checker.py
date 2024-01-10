from textblob import TextBlob

def predict_mood(text):
    # Create a TextBlob object
    blob = TextBlob(text)
    
    # Get the sentiment polarity
    polarity = blob.sentiment.polarity

    # Predict mood based on polarity
    if polarity > 0:
        return "Positive"
    elif polarity < 0:
        return "Negative"
    else:
        return "Neutral"

# Example usage
user_input = input("Enter a statement: ")
predicted_mood = predict_mood(user_input)
print(f"Predicted mood: {predicted_mood}")
