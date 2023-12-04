FROM ubuntu@sha256:b492494d8e0113c4ad3fe4528a4b5ff89faa5331f7d52c5c138196f69ce176a6 AS app

RUN apt-get update
RUN apt-get install -y make
RUN apt-get install -y gcc
RUN apt-get clean && rm -rf /var/lib/apt/lists/*;

ADD ./passgen /app/run
ADD ./flag.txt /app/
RUN chmod +x /app/run

FROM pwn.red/jail
COPY --from=app / /srv
ENV JAIL_TMP_SIZE=1024 JAIL_MEM=30M JAIL_TIME=60

EXPOSE 5000
