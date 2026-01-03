#!/bin/bash

cd "$(dirname "$0")/.."
export PYTHONPATH=$PYTHONPATH:$(pwd)

if [ -f .env ]; then
    set -a
    source .env
    set +a
fi

echo "Starting Assistant Server..."
python3 -m uvicorn app.main:app \
    --host ${APP_HOST:-0.0.0.0} \
    --port ${APP_PORT:-8000} \
    --log-level ${LOG_LEVEL:-info} \
    --proxy-headers \
    --forwarded-allow-ips='*'