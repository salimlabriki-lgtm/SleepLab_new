FROM mcr.microsoft.com/devcontainers/base:ubuntu

USER root

# Base tools + python + psql + utilitaires
RUN apt-get update && apt-get install -y \
    postgresql-client \
    python3 python3-pip python3-venv \
    git curl ca-certificates jq \
    && rm -rf /var/lib/apt/lists/*

# (Optionnel mais très utile) Jupyter/Papermill + libs data
RUN python3 -m pip install --no-cache-dir -U pip \
 && python3 -m pip install --no-cache-dir \
    pandas \
    psycopg2-binary \
    jupyter \
    papermill \
    nbconvert \
    ipykernel

# Important: on revient à l'user vscode
USER vscode
WORKDIR /workspaces
