# AI-Companion BE

## Overview
The AI-Companion backend is designed to serve as the core functionality for an AI-powered terminal assistant. This backend utilizes the Gemini API to process natural language inputs and generate contextually relevant responses, enabling users to engage in specialized conversations.

## Key Features
- **Flask Framework**: The backend is built using Flask, a lightweight WSGI web application framework.
- **CORS Support**: Flask-CORS is implemented to allow cross-origin requests, enabling the frontend to communicate with the backend seamlessly.
- **Environment Variables**: The application uses a `.env` file to securely manage API keys and other sensitive information.
- **Gemini API Integration**: The backend connects to the Gemini API to provide AI-generated responses based on user prompts.

## File Structure
- `app.py`: The main application file that contains the Flask application and API endpoint for handling requests.

## Usage
To run the backend:
1. Ensure you have the required packages installed:
   ```bash
   pip install Flask flask-cors python-dotenv google-generativeai
   ```
2. Set up your environment variables in a `.env` file, including your `API_KEY`.
3. Run the application:
   ```bash
   python app.py
   ```

The backend will be accessible at `http://127.0.0.1:5000/api/gemini-data` for POST requests.

## Conclusion
The AI-Companion backend is a crucial component of the AI assistant project, providing the necessary infrastructure to handle user interactions and generate intelligent responses using the Gemini API.