#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/" + user_id)
    TODO_keys = {"userId": user_id}
    tasks = requests.get("{}todos".format(URL), params=TODO_keys)
    name = user.json().get("username")
    lista = []

    for task in tasks.json():
        lista.append(dict(task=task.get("title"),
                           completed=task.get("completed"),
                           username=name))

    data = {argv[1]: lista}

    with open('{}.json'.format(user_id), 'w') as file:
        json.dump(data, file)
