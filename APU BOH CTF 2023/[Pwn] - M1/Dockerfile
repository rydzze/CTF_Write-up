FROM ubuntu@sha256:b492494d8e0113c4ad3fe4528a4b5ff89faa5331f7d52c5c138196f69ce176a6 AS chroot

RUN apt-get update
RUN apt-get install -y qemu-user-static
RUN apt-get install -y libc6-arm64-cross
RUN apt-get clean && rm -rf /var/lib/apt/lists/*;

ADD ./m1 /app/
ADD ./flag.txt /app/

RUN echo '#!/usr/bin/env bash\n\
    exec 2>/dev/null\n\
    exec /usr/bin/qemu-aarch64-static -L /usr/aarch64-linux-gnu/ ./m1\n\
    ' > /app/run
RUN chmod +x /app/run
RUN chmod +x /app/m1

FROM pwn.red/jail
COPY --from=chroot / /srv
ENV JAIL_TMP_SIZE=1024 JAIL_MEM=256M JAIL_TIME=60

EXPOSE 5000
