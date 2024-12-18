# LangChain Server

## Overview
This project implements a simple API server using LangChain runnable interfaces. The server is built with FastAPI and is designed to process user requests and generate outputs via a Groq-based LLM (Gemma2-9b-It).

## Features
- **Language Translation**: Translate input text into the desired language using Groq's language model.
- **Chain-Based Execution**: Combines prompts, models, and parsers for streamlined processing.
- **Extensible Architecture**: Built with LangChain and FastAPI for scalability and integration.

## Prerequisites
- Python 
- A valid Groq API key

## Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-directory>
   ```

2. **Set Up Environment**:
   Create a `.env` file and add your Groq API key:
   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

3. **Install Dependencies**:
   Use the following command to install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Start the Server**:
   Run the following command to start the FastAPI server:
   ```bash
   python app.py
   ```

2. **Access the API**:
   The API documentation will be available at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).

3. **Translation Endpoint**:
   Send POST requests to the `/chain` endpoint with the required input:
   ```json
   {
       "langauge": "desired_language",
       "text": "text_to_translate"
   }
   ```

## Project Structure

- **app.py**: The main application script that sets up the FastAPI server and LangChain chain.
- **requirements.txt**: A list of required Python packages.
- **.env.example**: A template for environment variable configuration.

## Dependencies
- `langchain`
- `python-dotenv`
- `langchain-community`
- `langchain-groq`
- `uvicorn`

## Acknowledgments
- [LangChain](https://www.langchain.com/)
- [Groq](https://www.groq.com/)
- [FastAPI](https://fastapi.tiangolo.com/)
