def hero(name):
    data={
        'spider-man': {'fname': 'Peter', 'lname': 'Parker'},
        'iron man': {'fname': 'Tony', 'lname': 'Stark'},
        'black widow': {'fname': 'Natasha', 'lname': 'Romanoff'}
    }
    return data[name]


if __name__ == "__main__":
    print(hero('black widow'))