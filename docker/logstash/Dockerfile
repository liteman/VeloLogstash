# Use the official Logstash Docker image as the base image
FROM docker.elastic.co/logstash/logstash:8.6.0

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Copy the Logstash pipeline configuration files (from a local folder) into the container
COPY pipeline.yml /usr/share/logstash/pipeline.yml
COPY logstash.yml /usr/share/logstash/config/logstash.yml
COPY ./resources/artifact_dictionary.json /usr/share/logstash/artifact_dictionary.json

RUN mkdir /usr/share/logstash/plugins
# Optionally, set permissions for the copied files
#RUN chown -R 1000:1000 /usr/share/logstash/
#RUN chmod -R 755 /usr/share/logstash/pipeline/

# Expose the ports that Logstash uses
#EXPOSE 5044 9600

# Set the default command to run Logstash with the default pipeline directory
CMD ["logstash"]