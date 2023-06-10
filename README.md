# Chat GPT Clone

This repository contains the code for a simplified version of OpenAI's GPT-3 powered chatbot. It has been designed to mimic the language processing capabilities of the official ChatGPT.

## Features

1. ChatGPT Clone responds to prompts entered by users.
2. It employs context and conversation history to provide relevant responses.
3. While it's not the official GPT-3 model, ChatGPT Clone strives to emulate its prowess in providing intelligent and contextually aware conversations.

## Usage

Just run the application, enter your prompts, and ChatGPT Clone will respond accordingly.

## Setup

1. Clone this repository to your local machine using the command:

```bash
git clone https://github.com/s6hib/Chat-GPT-Clone.git
```

2. Navigate to the cloned directory:

```bash
cd Chat-GPT-Clone
```

3. Set up a virtual environment to manage dependencies. If you're using `venv`, use the following commands:

```bash
python3 -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

### Setting up the API Key

This project uses the OpenAI API for language model capabilities. To use this API, you'll need an API key from OpenAI. Once you've obtained the key, set it up in your environment variables as `OPENAI_API_KEY`.

On Unix-based systems, you can add this line to your `.bashrc` or `.bash_profile`:

```bash
export OPENAI_API_KEY="your-api-key-here"
```

On Windows, you can add the environment variable through the system settings.

Replace `your-api-key-here` with your actual OpenAI API key.

Deactivate and reactivate your virtual environment to ensure the key is loaded:

```bash
deactivate
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```

### Running the Application

After setting up the API key, run the application with:

```bash
python main.py
```
