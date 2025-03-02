# Use the official Logstash Docker image as the base image
FROM docker.elastic.co/logstash/logstash:8.6.0

# Set environment variables to avoid interactive prompts
ENV DEBIAN_FRONTEND=noninteractive

# Copy the Logstash pipeline configuration files (from a local folder) into the container
COPY pipelines.yml /usr/share/logstash/pipelines.yml
COPY logstash.yml /usr/share/logstash/config/logstash.yml
COPY ./resources/artifact_dictionary.json /usr/share/logstash/artifact_dictionary.json
RUN rm -rf /usr/share/logstash/pipeline

RUN mkdir /usr/share/logstash/plugins
# Optionally, set permissions for the copied files
#RUN chown 1000:1000 /usr/share/logstash/pipelines.yml
#RUN chmod 755 /usr/share/logstash/pipelines.yml

# Expose the ports that Logstash uses
#EXPOSE 5044 9600

# Set the default command to run Logstash with the default pipeline directory
CMD ["logstash","--path.settings","/usr/share/logstash"]