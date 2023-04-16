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

TBC - diagram of application components and how data flows between them