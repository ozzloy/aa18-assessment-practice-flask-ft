#! /usr/bin/env bash

# initialize db
pipenv run flask db init

# this creates the up and down somehow
pipenv run flask db migrate -m "create simple_people table"

# this runs the up
pipenv run flask db upgrade
