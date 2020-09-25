import test

hellodict = {
    "English": "Hello",
    "Australian": "G'day",
    "French": "Bonjour", 
    "Spanish": "Hola",
    "Italian": "Ciao"} 

worlddict = {
    "English": "World",
    "Australian": "World", 
    "French": "Monde", 
    "Spanish": "El Mundo",
    "Italian": "Mondo"} 


def hello_world():
    print(hellodict["English"] + " " + worlddict["English"])

def bonjour_monde():
    print(hellodict["French"] + " " + worlddict["French"])

def hola_elmundo():
    print(hellodict["Spanish"] + " " + worlddict["Spanish"])

def ciao_mondo():
    print(hellodict["Italian"] + " " + worlddict["Italian"])

def gday_world():
    print(hellodict["Australian"] + " " + worlddict["Australian"])