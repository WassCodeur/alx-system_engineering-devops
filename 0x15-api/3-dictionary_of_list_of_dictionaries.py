#!/usr/bin/python3
import requests
import json


if __name__ == '__main__':
    filename = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/todos"
    userUrl = "https://jsonplaceholder.typicode.com/users/{}"
    resTodos = requests.get(url)
    todos = resTodos.json()
    list_ = []
    dic_tasks = {}
    for td in todos:
        dic_task = {}
        userId = int(td['userId'])
        resUsers = requests.get(userUrl.format(userId))
        user = resUsers.json()
        dic_task['username'] = user['username']
        dic_task['title'] = td['title']
        dic_task['completed'] = td['completed']
        list_.append(dic_task)
        if userId in dic_tasks:
            dic_tasks[userId].append(list_)
        else:
            dic_tasks[userId] = list_
    with open(filename, 'a') as f:
        f.write(json.dumps(dic_tasks))
