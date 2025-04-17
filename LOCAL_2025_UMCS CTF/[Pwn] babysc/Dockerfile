FROM ubuntu:22.04

# Install necessary dependencies
RUN apt-get update && apt-get install -y \
    socat \
    && rm -rf /var/lib/apt/lists/*

# Add a non-privileged user to run the challenge
RUN useradd -m pwnuser

# Set the working directory
WORKDIR /home/pwnuser

# Copy the source code and flag
COPY ./babysc /home/pwnuser/babysc
COPY ./flag /flag

# Expose the port
EXPOSE 10001

# Switch to the non-privileged user
USER pwnuser

# Start socat directly
CMD ["socat", "TCP-LISTEN:10001,reuseaddr,fork", "EXEC:/home/pwnuser/babysc"]

