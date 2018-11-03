# NxDraft
NxDraft does exactly what the name suggests; it creats N drafts from one.

## To Use

The client uses pipenv and google-api-python-client for it's working.

Below are the steps on how to use it:

- `pip install pipenv`
- go to project directory and run `pipenv shell --three`
- install all dependencies
    `pipenv install`
- run the project and follow the CLI
    `python3 nxdraft/api.py`

NOTE: The browser authentication is required only once, after that the secrets
are stored and used \[forever\].