FROM apache/superset:latest

USER root
# driver postgres + psql client si tu veux debug depuis le container
RUN /app/docker/pip-install.sh psycopg2-binary

USER superset
