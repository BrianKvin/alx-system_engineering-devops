#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress
"""
import requests
import sys

if __name__ == '__main__':
    user_id = sys.argv[1]
    # response = requests.get
    (f"https://jsonplaceholder.typicode.com/users/{user_id}")

    url = 'https://jsonplaceholder.typicode.com/users/{}'.format(user_id)
    response = get(url)
    name = response.json().get('name')
    url = 'https://jsonplaceholder.typicode.com/users/{}/todos'
    .format(user_id)
    response = get(url)
    tasks = response.json()
    done = 0
    done_tasks = []
    for task in tasks:
        if task.get('completed'):
            done_tasks.append(task)
            done += 1

    print("Employee {} is done with task({}/{}):"
        .format(name, done, len(tasks)))
    for task in done_tasks:
        print("\t {}".format(task.get('title')))
