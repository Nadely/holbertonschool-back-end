#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""


import json
import requests


def get_employee_todo_progress():
    url = 'https://jsonplaceholder.typicode.com/users'
    response = requests.get(url)

    if response.status_code == 200:
        users = response.json()

        todos_data = {}

        for user in users:
            user_id = user["id"]
            username = user["username"]

            url_todos = (
    f'https://jsonplaceholder.typicode.com/todos?userId='
    f'{user_id}'
)

            todos_response = requests.get(url_todos)

            if todos_response.status_code == 200:
                todos = todos_response.json()

                todos_data[user_id] = [
                    {"username": username, "task": todo["title"], "completed":
                     todo["completed"]} for todo in todos]

    json_variable = 'todo_all_employees.json'
    with open(json_variable, 'w', newline='') as jsonfile:
        json.dump(todos_data, jsonfile)


if __name__ == '__main__':
    get_employee_todo_progress()
