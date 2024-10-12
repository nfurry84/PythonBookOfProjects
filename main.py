"""This is a hello world style script"""
import os

def print_hi(name):
    """print hi says hello to input parameter"""
    print(f'Hi there, {name}')
    conf = os.environ.get('MY_GLOBAL_APP_VARIABLE') #osnow
    not_secret_value = os.environ.get('MS1234')
    print(f'Config: {conf}')
    print(f'Secret: {not_secret_value}')


if __name__ == '__main__':
    print_hi('Foo user')
