#!/usr/bin/python3

import argparse
import re
import os

parser = argparse.ArgumentParser(
    description='Parse docker-compose.yml file and prompt for present variables values to create .env'
)
parser.add_argument( 'composefile', help='docker-compose.yml')
args = parser.parse_args()

PATTERN = '\$\{?(\w+)(?::?-(\w+))?\}?'

def parse(compose_file):
    variables = {}
    for match in re.findall(PATTERN, compose_file):
        variables[match[0]] = match[1]
    return variables

def prompt(variables):
    results = {}
    for variable, default_value in variables.items():
        user_value = input("{} [{}]: ".format(variable, default_value))
        results[variable] = user_value if user_value else default_value
    return results

def toString(variables):
    return '\n'.join(['{}={}'.format(variable, value) for (variable, value) in variables.items()])

if __name__ == "__main__":

    compose_file_path = args.composefile
    env_file_path = os.path.join(os.path.dirname(compose_file_path), '.env')

    with open(compose_file_path, 'r') as compose_file, open(env_file_path, 'w') as env_file:
        variables = parse(compose_file.read())
        print("{} variables to define\n".format(len(variables)))
        variables = prompt(variables)
        env_file.write(toString(variables))
        print("\n .env file has been generated")
