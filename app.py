from flask import Flask, jsonify, request
from flask_cors import CORS
from dotenv import load_dotenv
import os
import google.generativeai as genai
from data.keywords import keywords
from data.validations import validate_relevance

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
    
    # combine prompt with keywords,
    keyword_str = " ".join(keywords)
    combined_prompt = f"{prompt} Context: {keyword_str}"
    
    # Create a generation_config dictionary with default values
    generation_config = {
        "temperature": 0.8,
        "max_output_tokens": 200
    }
    
    # Update generation_config with any provided kwargs
    generation_config.update(kwargs)
    
    response = model.generate_content(prompt, generation_config=generation_config)
    return response.text

# CAN YOU BEFORE_REQUEST IN FLASK FOR VALIDATIONS ACROSS ALL ROUTES:
#  Using a Flask Before Request Hook

@app.before_request
def validate_request():
    if request.method == "POST" and request.endpoint == "get_gemini_data":
        data = request.get_json()
        
        prompt = data.get("prompt")
        if not validate_relevance(prompt):
            return jsonify({"error": "Prompt is not relevant to The Sims 2 base game. Please adjust your prompt and try again."}), 400


@app.route("/api/gemini-data", methods=["POST"])
def get_gemini_data():
    data = request.get_json()
    prompt = data.get("prompt")
    
    # run validation function if not useing before_req above
    # is_relevant = validate_relevance(prompt)
    # if not is_relevant:
    #     return jsonify({"error": "Prompt is not relevant to The Sims 2 base game. Please adjust your prompt and try again."}), 400
    
    gemini_response = get_completion(prompt)
    
    return jsonify({"gemini": gemini_response}), 200

if __name__ == "__main__":
    app.run(debug=True)  # Enable debug mode for better error messages
