# Documentation

This documentation covers development as well as a basic user guide.

# Usage Guide

## Installation

Installation is done with Docker, one container for the app and one for the SQL server. Currently a WSGI server is *not* used, and the Flask development server is used instead - this will change.

git clone https://github.com/ashleycollinge1/Audiophile.git
docker-compose up -d

## Importing your first library

# Developer's Guide

## Environment Setup

    cd Audiophile/Audiophile
    python -m venv env/
    ./env/Scripts/activate.ps1
    pip install -r requirements.txt


    sudo apt install libmariadb3 libmariadb-dev

TBC - diagram of application components and how data flows between them

## Flask migrate

To apply new migrations to your db, use:

    flask db upgrade

Useful link: https://flask-migrate.readthedocs.io/en/latest/

## Useful links for dev

https://medium.com/@ilyas_24382/deploy-a-web-app-using-flask-and-docker-containers-96218e80e5fa

https://github.com/il-gen/basic_Docker-Flask
