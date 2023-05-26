#!/usr/bin/python3
"""
extend my pyrhon script to exprot data to a csv file
"""

from csv import DictWriter, QUOTE_ALL
import requests
from sys import argv


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
        todo_list = []
        for td in todos:
            todo_dict = {}
            cplt = td['completed']
            title = td['title']
            todo_dict['userId'] = userId
            todo_dict['username'] = usrname
            todo_dict['completed'] = cplt
            todo_dict['task'] = title
            todo_list.append(todo_dict)
        with open(filename, 'w') as f:
            header = ["userId", "username", "completed", "task"]
            wrtr = DictWriter(f, fieldnames=header, quoting=QUOTE_ALL)
            wrtr.writerows(todo_list)
