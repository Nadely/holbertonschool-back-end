#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import requests
from sys import argv


def get_employee_todo_progress(user_id):
    """Fetch and print TODO list progress for a given user_id"""

    # Fetch user details
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)

    if user_response.status_code == 200:
        user = user_response.json()
        user_name = user["name"]
        # Updated to fetch the correct field from the response

        # Fetch TODOs for the user
        todos_url = (
            f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')
        todos_response = requests.get(todos_url)

        if todos_response.status_code == 200:
            todos = todos_response.json()

            # Count completed tasks and gather their titles
            done_tasks = [todo["title"] for todo in todos if todo["completed"]]
            total_tasks = len(todos)

            print(f"Employee {user_name} is done with tasks
                  ({len(done_tasks)}/{total_tasks}):\n\t {', '.join(
                      done_tasks)}")


if __name__ == '__main__':
    # Ensure user_id is provided as an argument
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
        exit(1)

    get_employee_todo_progress(argv[1])
