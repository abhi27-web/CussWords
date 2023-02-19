from flask import Flask, request, jsonify
import profanity_check
import emoji

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_profanity():
    text = request.json['text']
    censored_text = profanity_check.censor(text)
    censored_text = emoji.emojize(censored_text, use_aliases=True)
    return jsonify({'censored_text': censored_text})

if __name__ == '__main__':
    app.run(port=8000)
