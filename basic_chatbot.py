def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    
    while True:
        user = input("You: ").lower()

        if user == "hello":
            print("Chatbot: Hi i am a chatbot!")

        elif user == "how are you":
            print("Chatbot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Chatbot: My name is SimpleBot. Create by Dev sharma.")

        elif user == "bye":
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
