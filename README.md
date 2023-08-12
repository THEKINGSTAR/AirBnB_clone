# 0x00. AirBnB clone - The console
# Background Context
## Welcome to the AirBnB clone project!

![Airbnb](https://github.com/Abdalmohsen-H/AirBnB_clone/assets/25788408/f6b79ba1-50c8-45f2-b3c4-11641e9a89a3)

## First step: Write a command interpreter to manage your AirBnB objects.
> ### This is the first step towards building your first full web application: the AirBnB clone. This first step is very important because you will use what you build during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…


## Python
console is used to interact with this AirBnb clone
instead of frontend

![cosole](https://github.com/Abdalmohsen-H/AirBnB_clone/assets/25788408/4f042332-953c-4bc2-b6de-9419f4aac9c9)

## Usage

How to use it
```shell
$ ./console.py
```
this will start command line interpeter

```shell
(hbnb) 
```

Now you have to use commands to ineract with console

command help will display availaple commands

```shell
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update
```

## Examples
```python
(hbnb) all
[]
(hbnb) create BaseModel
3ea9e8ed-f850-472a-ae23-46fc744130bb
(hbnb) all
["[BaseModel] (3ea9e8ed-f850-472a-ae23-46fc744130bb) {'id': '3ea9e8ed-f850-472a-ae23-46fc744130bb', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826440), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826458)}"]
(hbnb) show BaseModel 3ea9e8ed-f850-472a-ae23-46fc744130bb
[BaseModel] (3ea9e8ed-f850-472a-ae23-46fc744130bb) {'id': '3ea9e8ed-f850-472a-ae23-46fc744130bb', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826440), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826458)}
(hbnb) create User
fb008a1d-299a-4d6e-a5be-de76115d4d6e
(hbnb) all
["[BaseModel] (3ea9e8ed-f850-472a-ae23-46fc744130bb) {'id': '3ea9e8ed-f850-472a-ae23-46fc744130bb', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826440), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826458)}", "[User] (fb008a1d-299a-4d6e-a5be-de76115d4d6e) {'id': 'fb008a1d-299a-4d6e-a5be-de76115d4d6e', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 47, 844566), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 47, 844581)}"]
(hbnb) all BaseModel
["[BaseModel] (3ea9e8ed-f850-472a-ae23-46fc744130bb) {'id': '3ea9e8ed-f850-472a-ae23-46fc744130bb', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826440), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826458)}"]
(hbnb) all User
["[User] (fb008a1d-299a-4d6e-a5be-de76115d4d6e) {'id': 'fb008a1d-299a-4d6e-a5be-de76115d4d6e', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 47, 844566), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 47, 844581)}"]
(hbnb) update User fb008a1d-299a-4d6e-a5be-de76115d4d6e my_name "A. Hesham"
(hbnb) all User
["[User] (fb008a1d-299a-4d6e-a5be-de76115d4d6e) {'id': 'fb008a1d-299a-4d6e-a5be-de76115d4d6e', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 47, 844566), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 47, 844581), 'my_name': 'A. Hesham'}"]
(hbnb) destroy User fb008a1d-299a-4d6e-a5be-de76115d4d6e
(hbnb) all
["[BaseModel] (3ea9e8ed-f850-472a-ae23-46fc744130bb) {'id': '3ea9e8ed-f850-472a-ae23-46fc744130bb', 'created_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826440), 'updated_at': datetime.datetime(2023, 8, 12, 8, 59, 11, 826458)}"]
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help show
 show an instance(obj) of input class by
        Id given by user
        Like get resource by ID in any web API

        format : show BaseModel {id : int}
        example : show BaseModel 1234-1234-1234
        this will show an instance of BaseModel class

(hbnb) quit
```
