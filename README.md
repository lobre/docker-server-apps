# Docker server apps

Applications for docker with docker-compose.

## Media volume

Before all, it is important to create the shared data volume that will be used by some projects:

    docker volume create --name=media

Then subfolders can be created in this volume like:

 - Downloads
 - Movies
 - Series
 - Books

Becareful, these folders should have permissions 755.

### Backup media

    docker run --rm -v media:/dbdata -v $(pwd):/backup ubuntu tar cvf /backup/backup.tar /dbdata

## Configuration

Use `core_env.py` to generate secret `.env` file before starting apps.

If a `README.md` file exists in the app folder, there might be more steps to do before starting the app.

## Start containers

Launch a `docker-compose up -d` in the apps folders.
