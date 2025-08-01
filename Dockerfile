FROM python:3.13-slim

# Instala cron y dos2unix, elimina exim4
RUN apt-get update && apt-get install -y cron dos2unix && \
    apt-get remove -y exim4 exim4-base && \
    apt-get clean && apt-get autoremove -y && \
    rm -rf /var/lib/apt/lists/*

# Establece directorio de trabajo
WORKDIR /app

# Copia requirements y los instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto del proyecto y convierte a LF (formato UNIX)
COPY . .

# Convierte todos los archivos en /app a formato UNIX
RUN find /app -type f -exec dos2unix {} \;

# Asegura permisos del script principal
RUN chmod +x /app/run_bot.sh

# Copia el archivo de cron y asegura formato correcto
COPY crontab.txt /etc/cron.d/bot-cron
RUN dos2unix /etc/cron.d/bot-cron && \
    echo "" >> /etc/cron.d/bot-cron && \  
    chmod 644 /etc/cron.d/bot-cron && \
    crontab /etc/cron.d/bot-cron

# Archivos de log
RUN touch /var/log/cron_test.log /var/log/twitter_bot.log /var/log/heartbeat.log && \
    chmod 666 /var/log/*.log

# Healthcheck docker
HEALTHCHECK --interval=15m --timeout=10s --start-period=5s --retries=3 \
  CMD python3 /app/src/healthcheck.py || exit 1

# Corre cron en primer plano
CMD ["cron", "-f"]
