#!/usr/bin/python3
""" Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress

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
"""

#!/usr/bin/python3
"""
Uses the JSON placeholder api to query data about an employee
"""

from requests import get
from sys import argv

if __name__ == '__main__':
    main_url = 'https://jsonplaceholder.typicode.com'
    todo_url = main_url + "/user/{}/todos".format(argv[1])
    name_url = main_url + "/users/{}".format(argv[1])
    todo_result = get(todo_url).json()
    name_result = get(name_url).json()

    todo_num = len(todo_result)
    todo_complete = len([todo for todo in todo_result
                         if todo.get("completed")])
    name = name_result.get("name")
    print("Employee {} is done with tasks({}/{}):"
          .format(name, todo_complete, todo_num))
    for todo in todo_result:
        if (todo.get("completed")):
            print("\t {}".format(todo.get("title")))
