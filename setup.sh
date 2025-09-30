#!/bin/bash

echo "Setting up virtual environment..."
python3 -m venv venv || exit 1
source venv/bin/activate || exit 1

echo "Upgrading pip..."
pip install --upgrade pip

echo "Installing dependencies..."
pip install -r requirements.txt || exit 1

# Create the DB only if it doesn't exist in the project root
if [ ! -f demo.db ]; then
  echo "Creating demo.db..."
  python init_demo_db.py || exit 1
else
  echo "demo.db already exists; leaving it unchanged."
fi

echo "Setup complete."
