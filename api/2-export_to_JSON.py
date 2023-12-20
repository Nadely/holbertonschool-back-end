#!/usr/bin/python3
"""Write a Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

from sys import argv
import csv
import json
import requests


def get_employee_todo_progress(user_id):
    """get the response and format and write data to JSON"""

    # Fetch todos for the given user_id
    todos_url = (
        'https://jsonplaceholder.typicode.com/todos?userId={}'.format(user_id))
    todos_response = requests.get(todos_url)
    todos = todos_response.json()

    # Fetch user details for the given user_id
    user_url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    user_response = requests.get(user_url)
    user = user_response.json()

    username = user.get("username")
    id_user = user["id"]

    # Prepare data in the desired JSON format
    todos_data = [
        {
            "userId": id_user,
            "userName": username,
            "completed": todo["completed"],
            "title": todo["title"]
        }
        for todo in todos
    ]

    # Write data to JSON file
    json_filename = '{}.json'.format(user_id)
    with open(json_filename, 'w') as jsonfile:
        json.dump(todos_data, jsonfile)


if __name__ == '__main__':
    """main function"""
    # Ensure user_id is provided as an argument
    if len(argv) != 2:
        print("Usage: {} <user_id>".format(argv[0]))
        exit(1)

    get_employee_todo_progress(argv[1])
