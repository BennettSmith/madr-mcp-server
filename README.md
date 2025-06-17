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

## Visual Studio Code

This repository includes a `.devcontainer` folder so you can develop inside a
containerized environment using Visual Studio Code.

1. Install [Docker](https://www.docker.com/) and
   [Visual Studio Code](https://code.visualstudio.com/).
2. Install the following VS Code extensions:
   - [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack)
     (or at least **Remote - Containers**).
   - [Python](https://marketplace.visualstudio.com/items?itemName=ms-python.python).
   - [Docker](https://marketplace.visualstudio.com/items?itemName=ms-azuretools.vscode-docker) (optional but helpful).
3. Open this folder in VS Code and choose **Reopen in Container** when prompted.
   VS Code will build the development container defined in `.devcontainer/devcontainer.json`.
4. After the container is ready, you can use the integrated terminal to run
   `docker-compose up` for the development server or `pytest` to run tests.
5. Set breakpoints as usual and start the debugger using the Python extension to
   debug the Flask application inside the container.
