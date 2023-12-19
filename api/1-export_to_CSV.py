#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""


import csv
import requests
from sys import argv


def get_employee_todo_progress():
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)

    if response.status_code == 200:
        user = response.json()

        username = user["username"]

    url_todos = f'https://jsonplaceholder.typicode.com/todos?userId={user_id}'

    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    id_user = user["id"]

    input_variable = '{}.csv'.format(user_id)
    with open(input_variable, 'w', newline='') as csvfile:
        file_writer = csv.writer(csvfile)
        file_writer.writerow(["USER_ID", "USERNAME", "TASK_COMPLETED_STATUS",
                               "TASK_TITLE"])

        for todo in todos:
            file_writer.writerow([id_user, username, str(todo["completed"]),
                                   todo["title"]])


if __name__ == '__main__':
    get_employee_todo_progress()
