def convert(text):
    # Replace :) with 🙂 and :( with 🙁
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    return text

def main():
    # Prompt the user for input
    user_input = input("Enter text with emoticons: ")
    # Call convert function
    converted_text = convert(user_input)
    # Print the result
    print("Converted text:", converted_text)

if __name__ == "__main__":
    main()
