def hello(name,lang):
    greeting = {
        'en': 'Hello',
        'es': 'Hola',
        'fr': 'Bonjour',
        'de': 'Hallo'
    }
    return f"{greeting.get(lang, 'Hello')} {name}!"


def main():
    import argparse
    parser = argparse.ArgumentParser(description='Greet a user in different languages.')

    parser.add_argument("-n",'--name', metavar="name", help='Name of the user')
    parser.add_argument("-l",'--lang', metavar="language",choices= ["en","es", "fr", "de"] ,help='Language code (en, es, fr, de)', default='en')
    
    args = parser.parse_args()
    
    print(hello(args.name, args.lang))


if __name__ == '__main__':
    main()


# This code defines a command-line interface (CLI) for a simple greeting program.
# It uses the argparse module to parse command-line arguments and greet the user in different languages.
# The hello function takes a name and a language code, and returns a greeting message.
# The main function sets up the argument parser, defines the expected arguments (name and lang), and calls the hello function with the parsed arguments.
# The script can be run from the command line, and it will print a greeting message based on the provided name and language code.