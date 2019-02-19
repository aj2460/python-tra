def say_hi():
    print ("hello user")


def translate(phrase):
    translation=""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation=translation+"g"
        else:
            translation=translation+letter
    return translation


# phrase = "Hello World python"
# print(phrase.upper() + " programing")
# say_hi()

print(translate("How Are you"))
