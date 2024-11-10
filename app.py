from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os


import google.generativeai as genai
# retrieve apikey value from env file
load_dotenv()

api_key = os.getenv("API_KEY")

os.environ['API_KEY'] = api_key
genai.configure(api_key=os.environ['API_KEY'])
# print(api_key)

# route backend env
app = Flask(__name__)
CORS(app)

# gemini prompt function
def get_completion(prompt, model="gemini-1.5-flash", **kwargs):
    model = genai.GenerativeModel(model)
    
    # Create a generation_config dictionary with default values
    generation_config = {
        "temperature": 0.8,
        "max_output_tokens": 200
    }
    
    # Update generation_config with any provided kwargs
    generation_config.update(kwargs)
    
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text

@app.route("/api/gemini-data", methods=["POST"])
def get_gemini_data():
    data = request.get_json()
    prompt = data.get("prompt")
    # prompt = data.get("prompt")
    gemini_response = get_completion(prompt)
    
    return jsonify({"gemini": gemini_response})

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error messages
