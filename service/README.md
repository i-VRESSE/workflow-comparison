# Web service 

* fastapi as framework
* postgresql as structured storage
* accepts job descriptions 
  * submitted by a user
  * submitted by a robot
* does authentication using Orcid OpenID connect

Templates on https://fastapi.tiangolo.com/project-generation/ are old.
Try list at https://github.com/mjhea0/awesome-fastapi#boilerplate

## Try https://github.com/tiangolo/full-stack-fastapi-postgresql

```
pip install cookiecutter
mkdir bartender-tiangolo && cd bartender-tiangolo
cookiecutter https://github.com/tiangolo/full-stack-fastapi-postgresql
project_name [Base Project]: bartender
project_slug [bartender]: bartender
domain_main [bartender.com]: 
domain_staging [stag.bartender.com]: 
docker_swarm_stack_name_main [bartender-com]: 
docker_swarm_stack_name_staging [stag-bartender-com]: 
secret_key [changethis]: gfudhjgpiosauhgfvnspivubwenpfiubwfpisbfisduhfsidopahfa;d
first_superuser [admin@bartender.com]: 
first_superuser_password [changethis]: 
backend_cors_origins [["http://localhost", "http://localhost:4200", "http://localhost:3000", "http://localhost:8080", "https://localhost", "https://localhost:4200", "https://localhost:3000", "https://localhost:8080", "http://dev.bartender.com", "https://stag.bartender.com", "https://bartender.com", "http://local.dockertoolbox.tiangolo.com", "http://localhost.tiangolo.com"]]: 
smtp_port [587]: 
smtp_host []: 
smtp_user []: 
smtp_password []: 
smtp_emails_from_email [info@bartender.com]: 
postgres_password [changethis]: 
pgadmin_default_user [admin@bartender.com]: 
pgadmin_default_user_password [changethis]: 
traefik_constraint_tag [bartender.com]: 
traefik_constraint_tag_staging [stag.bartender.com]: 
traefik_public_constraint_tag [traefik-public]: 
flower_auth [admin:changethis]: 
sentry_dsn []: 
docker_image_prefix []: 
docker_image_backend [backend]: 
docker_image_celeryworker [celeryworker]: 
docker_image_frontend [frontend]: 

```

## Try https://github.com/s3rius/FastAPI-template

```
python3 -m venv env
. env/bin/activate
pip install -U pip wheel poetry
python3 -m pip install fastapi_template
python3 -m fastapi_template \
--name bartender \
--description 'Job middleware for i-VRESSE' \
--api-type rest \
--db postgresql \
--orm sqlalchemy \
--ci github \
--dummy-model \
--routers \
--migrations \
--quite
```

```
cd bartender
```

In side terminal
```
docker run -p "5432:5432" -e "POSTGRES_PASSWORD=bartender" -e "POSTGRES_USER=bartender" -e "POSTGRES_DB=bartender" postgres:13.6-bullseye
```

```
# fill db
alembic upgrade "head"
# start service in dev mode
poetry run python -m bartender
```

## Try https://github.com/Buuntu/fastapi-react
