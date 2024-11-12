FROM mongo:8.0.3

ENV TZ=America/Detroit

RUN apt-get install -y tzdata

RUN apt-get update && apt-get install -y cron

COPY --chmod=644 ./cronjob /etc/cron.d/cronjob

COPY --chmod=755 ./backup.sh /usr/local/bin/backup.sh

RUN crontab /etc/cron.d/cronjob

RUN touch /var/log/cron.log

RUN chmod 666 /var/log/cron.log