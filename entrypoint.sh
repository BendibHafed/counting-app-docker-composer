#!/bin/sh

if [ "$FLASK_ENV" = "development" ]; then
    echo "Starting in development mode..."
    python app.py
else
    echo "Starting in production mode with Gunicorn..."
    gunicorn -b 0.0.0.0:5000 app:app
fi
