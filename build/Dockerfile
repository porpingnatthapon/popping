FROM jenkins/jenkins:lts

USER root

# Install Docker CLI & add jenkins user to docker group
RUN apt-get update && \
    apt-get install -y docker.io && \
    usermod -aG docker jenkins



