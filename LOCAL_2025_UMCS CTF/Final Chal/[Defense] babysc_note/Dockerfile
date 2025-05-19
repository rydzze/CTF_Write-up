FROM ubuntu:22.04 AS app

FROM pwn.red/jail

COPY --from=app / /srv
COPY ./babysc_revenge /srv/app/run
COPY ./hook.sh /jail/hook.sh
EXPOSE 10001

RUN chmod +x /jail/hook.sh
RUN chmod +x /srv/app/run

# Jail environment settings
ENV JAIL_PORT=10001 \
    JAIL_MEM=256M \
    JAIL_ENV_NUM=5 \
    JAIL_PID=20 \
    JAIL_TIME=1200

