FROM node:24-bookworm-slim

USER root

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONUNBUFFERED=1
ENV VIRTUAL_ENV=/opt/media-venv
ENV PATH="/opt/media-venv/bin:/usr/local/bin:/usr/local/sbin:/usr/sbin:/usr/bin:/sbin:/bin"
ENV NODE_ENV=production
ENV N8N_RELEASE_TYPE=stable
ENV SHELL=/bin/sh

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
       ca-certificates \
       ffmpeg \
       python3 \
       python3-pip \
       python3-venv \
       tini \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m venv /opt/media-venv \
    && /opt/media-venv/bin/pip install --no-cache-dir --upgrade pip setuptools wheel \
    && /opt/media-venv/bin/pip install --no-cache-dir \
       yt-dlp \
       faster-whisper

RUN npm install --global n8n@2.37.10 \
    && npm cache clean --force

RUN mkdir -p /home/node/.n8n /vault /opt/media-pipeline \
    && chown -R node:node /home/node /opt/media-venv /opt/media-pipeline

COPY media-helper.js /opt/media-pipeline/media-helper.js
COPY transcribe.py /opt/media-pipeline/transcribe.py

RUN chown -R node:node /opt/media-pipeline

USER node

WORKDIR /home/node

EXPOSE 5678

ENTRYPOINT ["tini", "--"]
CMD ["n8n", "start"]
