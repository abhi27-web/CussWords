from flask import Flask, request
# from joblib import load
# from profanity_filter import ProfanityFilter

app = Flask(__name__)

@app.route('/profanity', methods=['POST'])
def sort():
    data = request.get_json()
    sentence = data['sentence']
#     pf = ProfanityFilter()
#     output = pf.censor(sentence)
    return sentence

if __name__ == '__main__':
    app.run(port=8000, debug=True)
