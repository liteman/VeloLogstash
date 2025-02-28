# Use the official Filebeat Docker image as the base image
FROM docker.elastic.co/beats/filebeat:8.6.0

# Copy your custom configuration file (mybeat.yml) into the container
# Handled by Docker-compose
COPY filebeat.yml /usr/share/filebeat/filebeat.yml

# Set the correct permissions for the file
#RUN chmod 644 /usr/share/filebeat/filebeat.yml

# Expose any ports you might need, e.g., the Beats input port (5044) if using Filebeat with Logstash

# Command to run Filebeat using the custom configuration file
CMD ["filebeat", "-e"]