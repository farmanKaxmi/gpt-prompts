from flask import Flask, request, jsonify
from chatbot import ChatbotAPI
import uuid
from marshmallow import ValidationError
from validation import PromptCreateSchema,PromptUpdateSchema
app = Flask(__name__)
chatbot = ChatbotAPI()

create_schema = PromptCreateSchema()
update_schema = PromptUpdateSchema()


# Create new prompt
@app.route('/prompts', methods=['POST'])
def create_prompt():
    try:
        data = request.get_json()
        create_schema.load(data)
        prompt_id = str(uuid.uuid4())
        prompt_text = data.get('prompt_text')
        chatbot.create_prompt(prompt_id, prompt_text)

        return jsonify(response="Prompt created successfully", message="Success", status_code=200), 200
    except ValidationError as err:
        return jsonify({"message": "Validation error", "errors": err.messages}), 400


# Update existing prompt
@app.route('/prompts/<promptId>', methods=['PATCH'])
def update_prompt(promptId):
    try:
        data = request.get_json()
        update_schema.load(data)
        new_prompt_text = data.get('new_prompt')
        if chatbot.update_prompt(promptId, new_prompt_text):
            return jsonify(response="Prompt updated successfully", message="Success", status_code=200), 200
        else:
            return jsonify(response="Prompt not found", message="Error", status_code=401), 400
    except ValidationError as err:
        return jsonify({"message": "Validation error", "errors": err.messages}), 400

# Delete prompt
@app.route('/prompts/<promptId>', methods=['DELETE'])
def delete_prompt(promptId):
    if chatbot.delete_prompt(promptId):
        return jsonify(response="Prompt deleted successfully", message="Success", status_code=200), 200
    else:
        return jsonify(response="Prompt not found", message="Error", status_code=404), 404


# Generate response from prompt
@app.route('/prompts/<promptId>/generate', methods=['GET'])
def generate_response(promptId):
    prompt_text = chatbot.get_prompt_text(promptId)
    if prompt_text is not None:
        response = chatbot.generate_response(prompt_text)
        return jsonify(status_code=200, message="Success", response=response), 200
    else:
        return jsonify(status_code=404, message="Error", response="Prompt not found"), 404


@app.route('/prompts', methods=['GET'])
def get_all_prompts():
    all_prompts = chatbot.load_prompts()["prompts"]
    if all_prompts:
        return jsonify(response=all_prompts, message="Success", status_code=200), 200
    else:
        return jsonify(response="No Prompt Found", message="Error", status_code=404), 404


if __name__ == '__main__':
    app.run(debug=True)
