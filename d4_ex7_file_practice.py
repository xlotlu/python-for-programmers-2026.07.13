# Exercițiu
# scrieți o funcție
def grep(fname, match):
    pass
# ce printează toate liniile din `fname`
# care conțin substring-ul `match`

def grep(fname, match):
    with open(fname) as f:
        for line in f:
            if match in line:
                print(line.removesuffix('\n'))

#grep('data/it-was.txt', 'season')


# Exercițiu:
# să încărcăm ceva dintr-un API
# și să salvăm pe disk:

import requests

TODOS_URL = "https://jsonplaceholder.typicode.com/todos"

def save_todos(url, file, completed=False):
    """
    Loads TODOs from `url` and saves their titles
    to `file`, each item per line.

    By default saves only the items that are not marked
    as completed.
    """

    resp = requests.get(url)
    todos = resp.json()

    with open(file, 'w', encoding='utf-8') as f:
        for todo in todos:
            if todo['completed'] is completed:
                f.write(todo['title'] + '\n')

        # alternativ, cu comprehension,
        # ba nu! cu generator expression:
        f.writelines(
            f"{t['title']}\n"
            for t in todos if not t['completed']
        )

#save_todos(TODOS_URL, "todos.txt")
