FROM mcr.microsoft.com/devcontainers/python:1-3.13-bookworm

RUN apt-get update \
  && apt-get install -y --no-install-recommends npm \
  && npm install --global markdownlint-cli2 \
  && rm -rf /var/lib/apt/lists/*
