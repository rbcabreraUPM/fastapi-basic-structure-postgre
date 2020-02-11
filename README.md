# fastapi-basic-structure-postgre
## Installation

Using pipenv

```bash
pipenv shell
pipenv install -r ./requirements.txt
```

## Connecting to PostgreSQL

create .env file inside /app and insert

```bash
DATABASE_URL='<your-postgre-url>'
```
## Run FastAPI server

```bash
uvicorn app.main:app --reload
```
