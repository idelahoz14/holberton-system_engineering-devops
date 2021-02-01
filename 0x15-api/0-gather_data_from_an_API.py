#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import requests
from sys import argv

if __name__ == "__main__":
    if argv[1]:
        user_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/" + user_id)
    TODO_keys = {"userId": user_id}
    tasks = requests.get("{}todos".format(URL), params=TODO_keys)
    number_of_tasks = len(tasks.json())
    name = user.json().get("name")
    done_tasks = 0

    for task in tasks.json():
        if task.get("completed"):
            done_tasks += 1

    print("Employee {} is done with tasks({}/{}):".format(name, done_tasks,
          number_of_tasks))

    for task in tasks.json():
        if task.get("completed"):
            print("\t ", end="")
            print(task.get("title"))
