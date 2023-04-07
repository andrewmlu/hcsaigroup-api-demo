import os
from flask import Flask, jsonify, request
from flask_cors import CORS
import openai
import anthropic

# if you don't have flask, flask_cors, enter to terminal: pip install flask flask_cors

app = Flask(__name__)
CORS(app)

openai.api_key = ""
client = anthropic.Client("")

@app.route('/gpt3.5', methods=['GET'])
def gpt3_5():
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "What is 2+2+2?"}],
        max_tokens=100,
        temperature=0.9,
    )
    response_content = response.choices[0].message.content
    return jsonify({"response": response_content})

@app.route('/claude', methods=['GET'])
def claude():
    completion = client.completion(
        prompt=f"{anthropic.HUMAN_PROMPT}Hi {anthropic.AI_PROMPT}",
        max_tokens_to_sample=500,
        model="claude-instant-v1.0",
    )
    return jsonify({"response": completion.completion})

@app.route('/api/chat/gpt3.5', methods=['POST'])
def chat_gpt3_5():
    message = request.json['message']
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "system", "content": "Talk in iambic pentameter."},
                  {"role": "user", "content": "Do not ever use iambic pentameter, use sentences only!"},
                  {"role": "assistant", "content": "Cool!"},
                  {"role": "user", "content": message}],
        max_tokens=100,
        temperature=0.9,
    )
    response_content = response.choices[0].message.content
    return jsonify({"response": response_content})

@app.route('/api/chat/claude', methods=['POST'])
def chat_claude():
    message = request.json['message']
    completion = client.completion(
        prompt=f"{anthropic.HUMAN_PROMPT}{message}{anthropic.AI_PROMPT}",
        max_tokens_to_sample=500,
        model="claude-instant-v1.0",
    )
    return jsonify({"response": completion['completion']})

if __name__ == '__main__':
    app.run(debug=True, port=3000)