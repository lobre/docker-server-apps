#!/bin/bash

[ $# -eq 0 ] && { echo "Usage: $0 user"; exit 1; }

htpasswd -n $1
