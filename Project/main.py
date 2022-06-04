import os, random, argparse, sys
from requests import get

parser = argparse.ArgumentParser() 
parser.add_argument('--ping') 
parser.add_argument('--ip')
parser.add_argument('--word')
args = parser.parse_args(sys.argv[1:])


if args.ping == 'ping':
    def action():
        for i in range(1, 11):
            ip = "10.82.225.%d" %(i)
            return1 = os.system('ping -t 5 -w 2 %s > /dev/null 2> /dev/null' %ip)

            if return1:
                print(ip, 'is down')
            else:
                print(ip, 'is up')
    action()    


if args.ip == 'ip':
    print('Public IP address is:', get('https://api.ipify.org').text)


if args.word == 'password':
    while True:
        print('Passwords Generator')
        chars = list('+-/*!&$#?=w@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890')
        length = int(input('Length password? '))
        random.shuffle(chars)
        pasw = ''.join([random.choice(chars) for x in range(length)])
        print(f'Your password - {pasw}')
        break