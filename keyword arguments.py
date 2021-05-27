# def greet_user(first_name, last_name):
#    print(f"Hi {first_name} {last_name}!")
#    print('Welcome aboard')


# print("Start")
# greet_user(last_name="smith", first_name="John")
# greet_user("mary", last_name="Smith")
# print("Finish")

## you can always place a positional argument before a keyword
## argument, but not vice versa

# def square(number):
#    return number * number


# number = int(input("Number: "))
# print(square(number))


def emoji_converter(message):
    words = message.split(" ")
    emojis = {
        ":)": "🙂",
        ":(": "😔"
    }
    output = ""
    for word in words:
        output += emojis.get(word, word) + " "
    return output


message = input(">")
print(emoji_converter(message))
