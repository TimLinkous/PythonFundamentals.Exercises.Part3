def greet(name):
    print("Hello, welcome to ZipCode", name,"!")

#greet("Tim")
#greet("Darth Vader")
#greet("Guido Van Rossum")

def language_input():
    selection = input("Please seclect your language: \nEnter 1 for Engish\nEnter 2 for Spanish\nEnter 3 for French\n")
    

    if selection == "1":
        name1 = input("Please enter your name.\n")
        english_greeting = "Hi " + name1 + ". Welcome to ZipCode."
        print(english_greeting)
    elif selection == "2":
        name2 = input("Por favor, escriba su nombre.\n")
        spanish_greetng = "Hola " + name2 + ". Bienvenido a ZipCode."
        print(spanish_greetng)
    elif selection == "3":
        name3 = input("S'il vous plaît entrez votre nom\n")
        french_greeting = "Bonjour " + name3 + ". Bienvenue à ZipCode."
        print(french_greeting)
    else:
        "Please try again\nInténtalo de nuevo\nVeuillez réessayer"

language_input()

"""def name_input():
    name = input("Please enter your name.\n")
    return name
    
greet(name_input())



def language_input():
    
    
    selection = input("Please seclect your language: \nEnter 1 for Engish\nEnter 2 for Spanish\nEnter 3 for French")
    return selection"""



