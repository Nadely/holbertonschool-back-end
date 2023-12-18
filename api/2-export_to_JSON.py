#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""


import requests
from sys import argv
import json


def get_employee_todo_progress():
    user_id = argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user = response.json()

        username = user["username"]


    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    id_user = user["id"]

    json_variable = '{}.json'.format(user_id)
    with open(json_variable, 'w', newline='') as jsonfile:
        json.dump({
            id_user: [
                {"task": todo["title"], "completed": todo["completed"],
                 "username": username} for todo in todos]}, jsonfile)

if __name__ == '__main__':
    get_employee_todo_progress()
