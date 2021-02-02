#!/usr/bin/python3
"""Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    URL = "https://jsonplaceholder.typicode.com/"
    user = requests.get(URL + "users/" + user_id)
    TODO_keys = {"userId": user_id}
    tasks = requests.get("{}todos".format(URL), params=TODO_keys)
    name = user.json().get("name")

    with open('{}.csv'.format(user_id), mode='w') as reader:
        writer = csv.writer(reader,
                            delimiter=',',
                            quotechar='"',
                            quoting=csv.QUOTE_ALL)

        for task in tasks.json():
            writer.writerow([user_id,
                            name,
                            task.get('completed'),
                            task.get('title')])
