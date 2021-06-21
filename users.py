import sys
import pyperclip
users = {}
with open("users.txt") as f:
    for line in f:
        (key, val) = line.split(' - ')
        users[key] = val.replace('\n', '')


def podajHaslo(username):
    if username in users:
        pyperclip.copy(users.get(username))
        print('ok')
    else:
        print(username in users)

podajHaslo(sys.argv[1])




