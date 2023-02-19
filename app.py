from flask import Flask, request
import profanity_check

app = Flask(__name__)

@app.route('/profanity', methods=['POST'])
def check_profanity():
    data = request.get_json()
    sentence = data['sentence']
    words = sentence.split()

    # Check for profanity in the sentence
    if profanity_check.predict(words):
        # Replace profanity with symbols
        cleaned_sentence = ""
        for word in words:
            if profanity_check.predict([word]):
                cleaned_sentence += "*" * len(word) + " "
            else:
                cleaned_sentence += word + " "
        return {"cleaned_sentence": cleaned_sentence.strip()}
    else:
        return {"cleaned_sentence": sentence}

if __name__ == '__main__':
    app.run(port=8000, debug=True)
