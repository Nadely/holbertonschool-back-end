#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""


import requests
from sys import argv


def get_employee_todo_progress():
    user_id = argv[1]

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)

    response = requests.get(url)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        user = response.json()

        user_name = user["name"]


    url_todos = 'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id)

    response_todos = requests.get(url_todos)
    todos = response_todos.json()

    total_tasks = len(todos)
    done_tasks = 0
    titles = []

    for todo in todos:
        if todo["completed"] == True:
            done_tasks += 1
            titles.append(todo["title"])

    space_sting = '\n\t '.join(titles)

    print("Employee {} is done with tasks ({}/{}):\n\t {}"
          .format(user_name, done_tasks, total_tasks, space_sting))

if __name__ == '__main__':
    get_employee_todo_progress()
