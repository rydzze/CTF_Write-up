FROM ubuntu@sha256:b492494d8e0113c4ad3fe4528a4b5ff89faa5331f7d52c5c138196f69ce176a6 AS chroot

ADD ./chal /app/run
ADD ./flag.txt /app
RUN chmod +x /app/run

FROM pwn.red/jail
COPY --from=chroot / /srv
ENV JAIL_MEM=30M JAIL_TIME=30

EXPOSE 5000
