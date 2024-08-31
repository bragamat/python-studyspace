#!/bin/bash
# set -x # debugging mode
# set -e # exit on end

activate_venv () {
  echo "Running . .venv/bin/activate";
  . .venv/bin/activate
}

activate_venv
echo "Subshell activated"
