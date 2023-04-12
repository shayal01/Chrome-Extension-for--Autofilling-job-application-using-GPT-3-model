import os
from flask import Flask,request,jsonify
import openai
app=Flask(__name__)
openai.api_key = os.environ.get('OPEN_AI_KEY')
@app.route('/answer', methods=['POST'])
def answer():
    data=request.get_json()
    response = openai.Completion.create(
        engine="davinci",
        prompt=data['prompt'],
        max_tokens=data['max_tokens'],
        n=data['n'],
        stop=data['stop'],
        temperature=data['temperature']
    )
    return jsonify(response.choices[0].text)
if __name__ == '__main__':
    app.run()