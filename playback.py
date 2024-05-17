def main():
    user_input = input("Enter some text: ")
    modified_input = user_input.replace(' ', '...')
    print("Modified text:", modified_input)

if __name__ == "__main__":
    main()
