#!/bin/bash

[ $# -eq 0 ] && { echo "Usage: $0 container"; exit 1; }

networks=`docker network ls | awk '{if (NR!=1) print $2}' | egrep -v "bridge|none|host"`
for network in $networks
do
  docker network connect $network $@ 2>/dev/null;
done
