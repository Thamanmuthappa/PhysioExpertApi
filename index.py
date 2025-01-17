from flask import Flask, render_template, request, jsonify
import pickle
from model import MedicalSpeciality

app = Flask(__name__)

transcript = ""
finalized_model = None

@app.route('/')
def hello():
    return "Hello! Use '/predict' POST method to send transcript and recrive data"

@app.route('/predict', methods=['POST'])
def getresult():
    content_type = request.headers.get('Content-Type')
    global transcript
    global finalized_model
    if (content_type == 'application/json'):
        if request.method == 'POST':
            data = request.get_json()
            transcript = data['transcript']
        
        # finalized_model = pickle.load(open('model.pkl', 'rb'))
        result = finalized_model.final_prediction(transcript)
        return jsonify(
            speciality=result,
        )
    else:
        return 'Error: Content-Type is not JSON!'

if __name__ == '__main__':
    finalized_model = pickle.load(open('model.pkl', 'rb'))
    app.run()