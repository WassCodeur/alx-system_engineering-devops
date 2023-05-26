#!/usr/bin/python3
import requests
from sys import argv
import json


if __name__ == '__main__':
    if len(argv) != 2:
        print("USAGE: python3 2-export_to_JSON.py userId\n or")
        print("./2-export_to_JSON.py userId")
    else:
        userId = argv[1]
        filename = "{}.json".format(userId)
        urlTodos = "https://jsonplaceholder.typicode.com/todos?userId={}"
        urlUser = "https://jsonplaceholder.typicode.com/users/{}"
        resTodos = requests.get(urlTodos.format(userId))
        resUser = requests.get(urlUser.format(userId))
        user = resUser.json()
        todos = resTodos.json()
        usrname = user['username']
        list_ = []
        dic_1 = {}
        for td in todos:
            dic_2 = {}
            cplt = td['completed']
            title = td['title']
            dic_2['task'] = title
            dic_2['completed'] = cplt
            dic_2['username'] = usrname
            list_.append(dic_2)
        dic_1[userId] = list_
        dicToJson = json.dumps(dic_1)
        with open(filename, 'a') as f:
            f.write(dicToJson)
