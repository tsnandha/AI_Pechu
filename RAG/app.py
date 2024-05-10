from flask import Flask, render_template, request, jsonify
from query_data import *

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    question = request.form['question'].strip()
    if question:
        # Here you can perform logic to get the response
        # For simplicity, let's just return a dummy response
        response = generate_dummy_response(question)
        return jsonify({'response': response})
    else:
        return jsonify({'error': 'Please enter a question.'})

def generate_dummy_response(question):
    # Dummy response generation logic
    #return "Response to '{}' goes here.".format(question)
    return query_rag(question)

if __name__ == '__main__':
    app.run(debug=True)
