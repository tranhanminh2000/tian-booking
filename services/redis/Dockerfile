# Use an official Redis image as the base
FROM redis/redis-stack-server:latest


# Optionally, you can run additional commands during the build process
RUN apt-get update && apt-get install -y sudo

# Expose Redis port (default: 6379)
EXPOSE 6379

# Optionally, you can specify a command to run when the container starts
ENTRYPOINT [ "redis-server" ]