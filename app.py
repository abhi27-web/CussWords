from flask import Flask, request
from profanity_filter import ProfanityFilter

app = Flask(__name__)

@app.route('/profanity', methods=['POST'])
def check_profanity():
    data = request.get_json()
    sentence = data['sentence']
    pf = ProfanityFilter()
    output = pf.censor(sentence)
    return output

if __name__ == '__main__':
    app.run(port=8000, debug=True)
