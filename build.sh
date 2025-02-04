#!/usr/bin/env bash
# Exit on error
set -o errexit


pip install -r requirements.txt

# Convert static asset files


# Apply any outstanding database migrations
python manage.py migrate
