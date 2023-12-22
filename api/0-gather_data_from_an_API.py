#!/usr/bin/python3
"""This script fetches and displays the TODO list progress for a
given employee ID."""

import requests
from sys import argv


def get_employee_todo_progress():
    """Fetch and print TODO list progress for a given user_id."""

    """response = user info"""
    user_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = requests.get(url)
    user = response.json()

    if response.status_code == 200:
        user = response.json()
        user_name = user["name"]

    """todos = todo info"""
    url_todos = (
        f'https://jsonplaceholder.typicode.com/todos?userId={user_id}')

    response_todos = requests.get(url_todos)
    todos = response_todos.json()


    task_completed = [task for task in todos if task['completed']]


    user_name = user["name"]
    len_completed_tasks = len(task_completed)
    total_todo = len(todos)

    print("Employee {} is done with tasks({}/{}):".format(
            user_name,
            len_completed_tasks,
            total_todo))

    for task in task_completed:
        print(f"\t {task['title']}")


if __name__ == '__main__':
    get_employee_todo_progress()
