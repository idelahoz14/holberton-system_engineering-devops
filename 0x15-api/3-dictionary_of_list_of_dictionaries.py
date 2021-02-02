#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests


if __name__ == "__main__":
    URL = "https://jsonplaceholder.typicode.com/"
    counter = len(requests.get(URL + "users").json())
    data = {}
    full_data = {}
    for i in range(0, counter):
        user = requests.get(URL + "users/" + str(i + 1))
        TODO_keys = {"userId": str(i + 1)}
        tasks = requests.get("{}todos".format(URL), params=TODO_keys)
        name = user.json().get("username")
        lista = []

        for task in tasks.json():
            lista.append(dict(task=task.get("title"),
                               completed=task.get("completed"),
                               username=name))

        data = {(i+1): lista}
        full_data.update(data)

        with open('todo_all_employees.json', 'w') as file:
            json.dump(full_data, file)
