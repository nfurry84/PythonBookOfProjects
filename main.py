"""This is a hello world style script"""
def print_hi(name):
    """print hi says hello to input parameter"""
    print(f'Hi there, {name}')
    conf = os.environ.get('MY_GLOBAL_APP_VARIABLE')
    secret_value = os.environ.get('MY_SECRET')
    print(f'Config: {conf}')
    print(f'Secret: {secret_value}')


if __name__ == '__main__':
    print_hi('Foo user')
