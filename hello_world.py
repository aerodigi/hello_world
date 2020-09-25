language_support = ["ENGLISH", "FRENCH", "JAPANESE"]


def hello_world():
    words = "G\'day, world!"
    print(words)

def bonjour_monde():
    words = "Bonjour Monde!"
    print(words)


def konnichiwa():
    words = "Konnichi wa!"
    print(words)


def select_language():
    user_response = input("Pick a language: ")
    if user_response.upper() in language_support:
        if user_response.upper() == "ENGLISH":
            hello_world()
        if user_response.upper() == "FRENCH":
            bonjour_monde()
        if user_response.upper() == "JAPANESE":
            konnichiwa()
    elif user_response.upper() == "LANGUAGES":
        for x in range(len(language_support)):
            print(language_support[x])
        select_language()
    else:
        print("This language is not currently supported.")


select_language()
