language_support = ["ENGLISH", "FRENCH", "JAPANESE"]


def hello_world():
    print("G\'day, world!")


def bonjour_monde():
    print("Bonjour Monde!")


def konnichiwa():
    print("Konnichi wa!")


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
