#!/bin/bash

if [[ $1 == 'all' ]]; then
    for directory in *; do
    if [ -d "${directory}" ]; then
        cd ${directory}

        echo -ne "\n###################################\n"
        echo "# ${directory} -> docker-compose ${@:2}"
        echo -ne "###################################\n\n"

        docker-compose ${@:2}

        cd ..
    fi
done
else
    cd $1
    docker-compose ${@:2} 
fi
