#!/usr/bin/python3
"""
extend my pyrhon script to exprot data to a csv file
"""

from sys import argv
import requests


if __name__ == '__main__':
    if len(argv) != 2:
        print("USAGE : pyton3 1-export_to_CSV.py userId\n or")
        print("./1-export_to_CSV.py userId")
    else:
        userId = argv[1]
        filename = "{}.csv".format(userId)
        urlTodos = "https://jsonplaceholder.typicode.com/todos?userId={}"
        urlUsers = "https://jsonplaceholder.typicode.com/users/{}"
        resUser = requests.get(urlUsers.format(userId))
        user = resUser.json()
        usrname = user['username']
        resTodos = requests.get(urlTodos.format(userId))
        todos = resTodos.json()
        for td in todos:
            cplt = td['completed']
            title = td['title']
            line = '"{}","{}","{}","{}"\n'.format(userId, usrname, cplt, title)
            with open(filename, 'a') as f:
                f.write(line)
