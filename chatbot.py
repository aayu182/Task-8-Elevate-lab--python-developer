# Rule-Based Chatbot using if-else

def chatbot():
    print("ChatBot: Hello! I am your simple rule-based chatbot.")
    print("ChatBot: Type 'exit' to end the chat.\n")

    while True:
        user = input("You: ").lower().strip()

        # Exit command
        if user == "exit":
            print("ChatBot: Goodbye! Have a great day!")
            break

        # Basic rule-based responses
        elif "hello" in user or "hi" in user:
            print("ChatBot: Hello! How can I help you today?")

        elif "how are you" in user:
            print("ChatBot: I'm doing great! Thanks for asking.")

        elif "name" in user:
            print("ChatBot: I'm a simple chatbot created using Python.")

        elif "help" in user:
            print("ChatBot: You can ask me simple questions like:")
            print("        'hello', 'how are you', 'your name', etc.")

        else:
            print("ChatBot: Sorry, I didn't understand that.")

if __name__ == "__main__":
    chatbot()
