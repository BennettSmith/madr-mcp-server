# MADR MCP Server

This project is a skeleton for a Flask-based server that will process MADR documents.

## Development

Development is containerized. Use [Docker](https://www.docker.com/) to build and run the application:

```bash
# Build the development image
$ docker-compose build

# Run the server in development mode
$ docker-compose up
```

The application will be available at `http://localhost:5000/health`.

### Running Tests

```bash
$ docker-compose run --rm app pytest
```
