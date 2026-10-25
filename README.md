# Containerized Student Information API

A REST API built with Flask and packaged using Docker. It provides endpoints to retrieve student information and check API health.

## Features

- Retrieve API information.
- Check API health.
- List all students.
- Retrieve a student by ID.
- Return appropriate HTTP status codes for successful requests and errors.
- Run the API inside a Docker container using Gunicorn.

## Technology Stack

- Python 3.12 (inside Docker)
- Flask
- Gunicorn
- Docker

## API Endpoints

| Method | Endpoint | Description |
|-----|-----|-----|
| GET | `/` | Returns API information and available endpoints |
| GET | `/health` | Checks API health |
| GET | `/students` | Returns all student records |
| GET | `/students/<id>` | Returns a student by ID |

## Run with Docker

### 1. Build the image

```bash
docker build -t student-information-api .
```

### 2. Start the container

```bash
docker run --rm -p 5000:5000 student-information-api
```

### 3. Test the API

Open these URLs in your browser:

- `http://localhost:5000/`
- `http://localhost:5000/health`
- `http://localhost:5000/students`
- `http://localhost:5000/students/1`

## Example Response

A successful request to `/health` returns:

```json
{
  "status": "healthy"
}
```

## Error Handling

- `200 OK` — Request completed successfully.
- `400 Bad Request` — Student ID must be a positive integer when this validation is reached.
- `404 Not Found` — No student exists with the requested ID.

## Notes

- Student records are stored in memory.
- Student data resets when the application restarts.
- This project uses an in-memory list rather than a database.
