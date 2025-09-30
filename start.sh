#!/bin/bash

# This script is intended to be sourced so that the activated environment persists.
# Usage: source startup.sh

# Check if the script is being sourced.
if [[ "${BASH_SOURCE[0]}" == "${0}" ]]; then
  echo "Please source this script (e.g., 'source startup.sh') so that the environment remains activated."
  exit 1
fi

# Activate the virtual environment
if [ -f venv/bin/activate ]; then
  echo "Activating virtual environment..."
  source venv/bin/activate
else
  echo "Virtual environment not found. Please run setup.sh first."
  return 1
fi

echo ""
echo "Environment activated! Starting MCP server..."
echo ""

python mcp_server_example.py
