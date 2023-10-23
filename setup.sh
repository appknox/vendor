#!/bin/bash

# Check if Poetry is installed, if not, suggest installing via pipx
if ! command -v poetry &> /dev/null; then
    echo "Poetry is not installed."
    echo "We recommend installing Poetry via pipx, a tool to install and run Python applications in isolated environments."
    echo "After installing pipx, you can install Poetry by running: "
    echo "  pipx install poetry"
    exit 1
fi

# Create a virtual environment using Poetry
poetry install

# Initialize pre-commit hooks
echo "Initializing pre-commit hooks..."
poetry run pre-commit install

# Provide instructions to the user
echo "Setup complete! Your development environment is configured."
