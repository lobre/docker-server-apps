#!/bin/bash

if [[ -z $2 ]]; then
    for directory in *; do
    if [ -d "${directory}" ]; then
        cd ${directory}
        docker-compose $1
        cd ..
    fi
done
else
    cd $1
    docker-compose $2 
fi
