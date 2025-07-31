FROM python:3.13-slim

RUN apt-get update && apt-get install -y cron && apt-get clean

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

COPY .env .env

COPY crontab.txt /etc/cron.d/bot-cron
RUN chmod 644 /etc/cron.d/bot-cron && crontab /etc/cron.d/bot-cron
RUN chmod +x /app/run_bot.sh

CMD ["cron", "-f"]

