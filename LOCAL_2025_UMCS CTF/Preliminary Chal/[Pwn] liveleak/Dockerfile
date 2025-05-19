FROM ubuntu:22.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    socat \
    && rm -rf /var/lib/apt/lists/*

# Add a non-privileged user to run the challenge
RUN useradd -m pwnuser

WORKDIR /home/pwnuser/
# Copy the source code and flag
COPY ./libc.so.6 /home/pwnuser/libc.so.6
COPY ./ld-2.35.so /home/pwnuser/ld-2.35.so
COPY ./chall /home/pwnuser/chall
COPY ./flag /flag

# Expose the port
EXPOSE 10007

# Switch to the non-privileged user
USER pwnuser

# Start socat directly
CMD ["socat", "TCP-LISTEN:10007,reuseaddr,fork", "EXEC:/home/pwnuser/chall"]

