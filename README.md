# ToDo FastAPI Application

This is a simple ToDo application built using FastAPI, SQLAlchemy, and Docker.

## Project Structure

The project is structured as follows:

- `lib/`: Contains modules for CRUD operations, models, and database initialization.
- `main.py`: The main FastAPI application script.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Python dependencies.


# ToDo FastAPI Application

This is a simple ToDo application built using FastAPI, SQLAlchemy, and Docker.

## Project Structure

The project is structured as follows:

- `lib/`: Contains modules for CRUD operations, models, and database initialization.
- `main.py`: The main FastAPI application script.
- `Dockerfile`: Docker configuration file.
- `requirements.txt`: Python dependencies.

## Requirements

- Python 3.10 or higher
- Docker (optional)

## Getting Started

### Local Development

1. Install dependencies:

   ```bash
   pip install -r requirements.txt
Run the FastAPI application:

   ```bash
python main.py
```
The Swagger documentation will be available at http://127.0.0.1:8000/docs.

### Docker
Build the Docker image:

```bash
docker build -t todo-fastapi .
```
Run the Docker container:
```bash
docker run -p 8000:8000 todo-fastapi
```
The FastAPI application will be accessible at http://127.0.0.1:8000/docs.

### Example Usage
You can use tools like curl, httpie, or any API client to interact with the API. Here's an example using httpie:

```bash
# Create a new task
http POST http://127.0.0.1:8000/tasks/ title="Sample Task" description="This is a sample task"

# Retrieve all tasks
http GET http://127.0.0.1:8000/tasks/

# Retrieve a specific task by ID
http GET http://127.0.0.1:8000/tasks/{task_id}

# Update a task by ID
http PUT http://127.0.0.1:8000/tasks/{task_id} title="Updated Task" description="Updated description" status=true

# Delete a task by ID
http DELETE http://127.0.0.1:8000/tasks/{task_id}
Feel free to explore and customize the API according to your needs.
```
API application will be accessible at http://127.0.0.1:8000/docs.