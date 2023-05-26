#!/usr/bin/python3
import requests
from sys import argv
"""
a Python script that, using this REST API,
for a given employee ID, returns information
about his/her TODO list progress.
"""


if __name__ == '__main__':
    if len(argv) != 2:
        print("USAGE : python3 0-gather_data_from_an_API.py userId\n or")
        print("./0-gather_data_from_an_API.py userId")
    else:
        userId = argv[1]
        urlTodo = "https://jsonplaceholder.typicode.com/todos?userId={}"
        urlUser = "https://jsonplaceholder.typicode.com/users/{}"
        res = requests.get(urlTodo.format(userId))
        resEmployee = requests.get(urlUser.format(userId))
        completeTasks = []
        employee = resEmployee.json()
        todos = res.json()
        for todo in todos:
            if todo['completed']:
                completeTasks.append(todo)
        cpltTasksSize = len(completeTasks)
        tdsSize = len(todos)
        text = "Employee {} is done with tasks({}/{})"
        print(text.format(employee['name'], cpltTasksSize, tdsSize))
        for tasks in completeTasks:
            print("\t {}".format(tasks['title']))
