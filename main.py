"""This is a hello world style script"""
import os
CONF = ''
KEY = ''


def print_hi(name):
    """print hi says hello to input parameter"""
    print(f'Hi there, {name}')
    CONF = os.environ.get('MY_GLOBAL_APP_VARIABLE') #osnow
    KEY = os.environ.get('MY_SECRET')
    
    dowork(conf,key)
    #print(f'Config: {conf}')
    #print(f'Secret: {not_secret_value}')

def dowork(x,y):
    print(f'{x} : {y}')

if __name__ == '__main__':
    print_hi('Foo user')
