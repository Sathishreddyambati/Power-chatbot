from transformers import pipeline

# Load once
chatbot = pipeline("text2text-generation", model="google/flan-t5-small")

def get_bot_response(user_input):
    result = chatbot(user_input, max_length=100, do_sample=True)
    return result[0]['generated_text']