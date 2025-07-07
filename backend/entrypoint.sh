#!/bin/sh

# Aplica as migrations
flask db upgrade

# Inicia o servidor Flask
exec flask run --host=0.0.0.0
