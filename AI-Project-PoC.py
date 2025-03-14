import requests
import json
from openai import OpenAI

def generate_feedback(prompt: str, api_key: str) -> str:
    """
    Sends a prompt to an AI API and returns the generated feedback.

    Args:
        prompt (str): The input prompt for the AI.
        api_key (str): The API key used for authentication.

    Returns:
        str: The AI-generated feedback.
    """
    # Define the API endpoint for chat completions (using OpenAI's API as an example)
    api_url = "https://api.openai.com/v1/chat/completions"
    
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }
    
    # Configure the request payload
    data = {
        "model": "gpt-4",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7,
        "max_tokens": 256
    }
    
    response = requests.post(api_url, headers=headers, data=json.dumps(data))
    
    if response.status_code != 200:
        raise Exception(f"Request failed with status code {response.status_code}: {response.text}")
    
    result = response.json()
    # Extracting the AI's response from the result
    output = result["choices"][0]["message"]["content"]
    return output

if __name__ == "__main__":
    # Retrieve the prompt from another tool or source.
    # For demonstration, this is set to a static prompt.
    prompt_input = "What are the benefits of integrating AI in modern web applications?"
    
    # Your AI API key (replace with your actual API key)
    api_key = "your_api_key_here"
    
    print("Sending prompt to AI API...")
    feedback = generate_feedback(prompt_input, api_key)
    
    # Output the feedback which can be easily retrieved
    print("Generated Feedback:")
    print(feedback)
