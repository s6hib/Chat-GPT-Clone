from flask import Flask, request, jsonify
import openai
import os

my_secret = os.environ['OPENAI_API_KEY']

app = Flask(__name__, static_folder='static', template_folder='templates')

# Global dictionary to store conversation history
conv_history = {}


@app.route('/')
def home():
  return app.send_static_file('index.html')


@app.route('/message', methods=['POST'])
def message():
  data = request.get_json()
  user_message = data['message']
  session_id = request.remote_addr  # Using the remote IP address as the identifier

  # Check if there's history for this session
  if session_id not in conv_history:
    conv_history[session_id] = []

  # Append the user's message to the chat history
  conv_history[session_id].append({"role": "user", "content": user_message})

  # Generate AI's response
  ai_message = generate_response(user_message)

  # Append the AI's message to the chat history
  conv_history[session_id].append({"role": "assistant", "content": ai_message})

  return jsonify({'message': ai_message})


def generate_response(query):
  session_id = request.remote_addr
  # Start with a system message
  messages = [{
    "role":
    "system",
    "content":
    "You are a helpful assistant, ready to provide information and assist with various tasks."
  }]
  # Add the conversation history for this session
  messages.extend([{
    "role": msg["role"],
    "content": msg["content"]
  } for msg in conv_history[session_id]])
  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=messages)
  return response['choices'][0]['message']['content']


@app.route('/get_history', methods=['GET'])
def get_history():
  session_id = request.remote_addr
  if session_id in conv_history:
    return jsonify({'history': conv_history[session_id]})
  else:
    return jsonify({'history': []})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
