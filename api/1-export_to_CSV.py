#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import csv
import requests
from sys import argv


def get_employee_todo_progress(user_id):
    """get the response and format and write data to CSV"""

    todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    username = user.get("username")
    data_user = []

    for todo in todos:
        newrow = [todo.get("userId"), username, todo.get("completed"),
                  todo.get("title")]
        data_user.append(newrow)

    file_name = '{}.csv'.format(user_id)
    with open(file_name, mode='w') as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        writer.writerows(data_user)

        print(f"Data has been exported to {argv[1]}.csv")


if __name__ == '__main__':
    """main function"""
    get_employee_todo_progress(argv[1])
