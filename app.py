from flask import Flask, request
from better_profanity import profanity

app = Flask(__name__)

@app.route('/profanity', methods=['POST'])
def check_profanity():
    data = request.get_json()
    sentence = data['sentence']
    output = profanity.censor(item.Text)
    return output

if __name__ == '__main__':
    app.run(port=8000, debug=True)
