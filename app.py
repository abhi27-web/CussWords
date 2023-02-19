from flask import Flask, jsonify, request
from profanity_filter import ProfanityFilter

app = Flask(__name__)

@app.route('/profanity', methods=['POST'])
def check_profanity():
    data = request.get_json()
    sentence = data['sentence']
    pf = ProfanityFilter()
    output = pf.censor(sentence)
    return jsonify({'result': output})

if __name__ == '__main__':
    app.run()
