def get_jokes():
    return [
        ("Why do programmers prefer dark mode?", "Because light attracts bugs!"),
        ("Why was the JavaScript developer sad?", "Because he didn't Node how to Express himself!"),
        ("How many programmers does it take to change a light bulb?", "None, that's a hardware problem!"),
        ("Why don't programmers like nature?", "It has too many bugs!"),
        ("What do you call a programmer from Finland?", "Nerdic."),
        ("Why do programmers always mix up Halloween and Christmas?", "Because Oct 31 equals Dec 25."),
        ("What's a programmer's favorite hangout place?", "The Foo Bar."),
        ("How do you explain the movie Inception to a programmer?", "Basically, it's a function within a function within a function."),
        ("Why do Java developers wear glasses?", "Because they can't C#!"),
        ("What's a bug report?", "The only thing you'll ever write that your users will read enthusiastically!")
    ]

def display_jokes(jokes):
    for idx, (setup, _) in enumerate(jokes, 1):
        print(f"{idx}. {setup}")

def main():
    jokes = get_jokes()
    while True:
        print("\nChoose a joke number (1-10):")
        display_jokes(jokes)

        try:
            choice = int(input("Your choice: "))
            if 1 <= choice <= 10:
                setup, punchline = jokes[choice - 1]
                print(f"{setup} -> {punchline}")
            else:
                print("Please choose a number between 1 and 10.")
                continue
        except ValueError:
            print("Please enter a valid number.")
            continue

        continue_fun = input("\nDo you want the fun to continue? (yes/no): ").lower()
        if continue_fun != 'yes':
            print("Thanks for your time. Enjoy!")
            break
        else:
            print("\nGreat!!!")

if __name__ == "__main__":
    main()
