FROM mcr.microsoft.com/devcontainers/base:ubuntu

# Paquets de base : client Postgres + Python
RUN apt-get update && \
    apt-get install -y \
        postgresql-client \
        python3 \
        python3-pip \
    && rm -rf /var/lib/apt/lists/*

# User par défaut
USER vscode

# Dossier de travail générique (VS Code utilisera workspaceFolder)
WORKDIR /workspaces
