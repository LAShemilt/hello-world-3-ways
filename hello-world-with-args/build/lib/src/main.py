import click

def print_hi(name):
    greeting = f'Hi, {name}'
    print(greeting)
    return greeting
def save_greeting(fname, greeting):
    with open (fname, 'w') as f:
        f.writelines(greeting)
@click.command()
@click.option('--name', default="World", help='The person you want to greet.')
@click.option('--fname', default=None, help='The path you want to save the greeting to')
def greet(name, fname=None):

    try:
        greeting = print_hi(name)
    except:
        greeting = None
        print("No name provided could not greet")

    if fname and greeting:
        save_greeting(fname, greeting)

if __name__ == '__main__':
    greet()


