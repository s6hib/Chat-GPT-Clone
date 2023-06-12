from flask import Flask, request, jsonify, session
import openai
import os

my_secret = os.environ['OPENAI_API_KEY']

app = Flask(__name__, static_folder='static', template_folder='templates')

# Set secret key for sessions
app.secret_key = 'supersecretkey'


@app.route('/')
def home():
  return app.send_static_file('index.html')


@app.route('/message', methods=['POST'])
def message():
  data = request.get_json()
  user_message = data['message']

  # If 'chat_history' not in session, create a new list
  if 'chat_history' not in session:
    session['chat_history'] = [{
      "role": "system",
      "content": "You are a helpful assistant."
    }]

  # Append the user's message to the chat history
  session['chat_history'].append({"role": "user", "content": user_message})

  response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                          messages=session['chat_history'])

  # Get AI's message
  ai_message = response['choices'][0]['message']['content']

  # Append the AI's message to the chat history
  session['chat_history'].append({"role": "assistant", "content": ai_message})

  return jsonify({'message': ai_message})


@app.route('/get_history', methods=['GET'])
def get_history():
  if 'chat_history' in session:
    return jsonify({'history': session['chat_history']})
  else:
    return jsonify({'history': []})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
