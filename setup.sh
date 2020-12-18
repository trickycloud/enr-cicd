#!/bin/sh

sudo chmod +777 -R /var/lib/jenkins/workspace/

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    virtualenv env
fi

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

chmod -R 777 logs