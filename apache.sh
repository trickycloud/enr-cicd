#!/bin/sh

sudo rm /etc/apache2/sites-available/000-default.conf

sudo cp -rf 000-default.conf /etc/apache2/sites-available

sudo service apache2 restart