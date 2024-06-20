import re


def get_response(user_input):
    # Convert the input to lowercase for case-insensitive matching
    user_input = user_input.lower()

    # Define some basic responses
    if re.search(r'\bhello\b|\bhi\b|\bhey\b', user_input):
        return "Hello! How can I help you today?"
    elif re.search(r'\bhow are you\b', user_input):
        return "I'm just a bot, but I'm doing great! How about you?"
    elif re.search(r'\bweather\b', user_input):
        return "I'm not sure about the weather, but you can check a weather app or website for the latest updates."
    elif re.search(r'\bname\b', user_input):
        return "I'm a simple chatbot created to help you with basic queries."
    elif re.search(r'\bhelp\b|\bassistance\b', user_input):
        return "Sure! I'm here to help. You can ask me about the weather, my name, or how I'm doing."
    elif re.search(r'\bbye\b|\bexit\b|\bquit\b', user_input):
        return "Goodbye! Have a great day!"
    else:
        return "I'm sorry, I don't understand that. Can you please rephrase?"


def chat():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        response = get_response(user_input)
        print(f"Chatbot: {response}")
        if re.search(r'\bbye\b|\bexit\b|\bquit\b', user_input.lower()):
            break


# Start the chatbot
chat()
