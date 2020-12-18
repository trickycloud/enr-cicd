#!/bin/bash

source ./env/bin/activate

pip install -r requirements.txt

pip3 install django

python3 manage.py makemigrations

python3 manage.py migrate




