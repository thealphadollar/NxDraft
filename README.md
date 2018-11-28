# NxDraft

[![Join the chat at https://gitter.im/NxDraft/Lobby](https://badges.gitter.im/NxDraft/Lobby.svg)](https://gitter.im/NxDraft/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

NxDraft does exactly what the name suggests; it creats N drafts from one.

## To Use

The client uses pipenv and google-api-python-client for it's working.

### First Run

Below are the steps on how to use it **for the first time**:

- `pip install pipenv`
- go to project directory and run `pipenv shell --three`
- install all dependencies
    `pipenv install`
- run the project and follow the CLI
    `python3 nxdraft/api.py`

NOTE: The browser authentication is required only once, after that the secrets
are stored and used \[forever\].

### Consecutive Run

Below are the steps that need to be followed if you've already ran the program once.
- `cd /to/project/directory`
- `pipenv shell`
- `python3 nxdraft/api.py`

The virtual environment created in first step is used here :)
