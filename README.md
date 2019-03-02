# Bailiwick

Bailiwick is a web-based tool for creating a mock version of the real-world DNS hierarchy for training and education purposes.

# Installation

Follow these instructions to get the project up and running in your own development environment.

1. Clone the project.
   ```bash
   $ git clone https://github.com/Raznic/Bailiwick
   $ cd Bailiwick/src/
   ```
2. Optionally, create a [Python virtual environment](https://packaging.python.org/guides/installing-using-pip-and-virtualenv/).  Though not required, it is recommended to help keep this project's dependencies isolated from other Python projects on the same system which may have different packages or package versions.
3. Install package requirements.
   ```bash
   $ pip install -r requirements.txt
   ```
4. Run any database migrations.
   ```bash
   $ python manage.py migrate
   ```
5. Launch the development server.
   ```bash
   $ python manage.py runserver
   ```
   
# Tests

To run tests for the project, use the following command:

```bash
$ python manage.py test
```

# Contributing

Contributions to the project in any form are always welcome. Please read the [contributing guidelines](CONTRIBUTING.md) for details.