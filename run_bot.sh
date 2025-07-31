#!/bin/bash

set -a
source /app/.env
set +a

cd /app/src
python3 -m twitter_bot.bot
