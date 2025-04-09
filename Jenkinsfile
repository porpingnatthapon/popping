pipeline {
    agent any

    environment {
        IMAGE_NAME = "my-python-app"
        VERSION = "0.0.${env.BUILD_NUMBER}"
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Checking out source code...'
                checkout scm
            }
        }

        stage('Install & Unit Test') {
            steps {
                echo 'Running unit tests inside Python container...'
                sh '''
                    docker run --rm \
                        -v "$PWD":/app \
                        -w /app \
                        python:3.11-slim \
                        sh -c "pip install --upgrade pip && python -m unittest discover -s . -p 'test_*.py'"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Building Docker image: ${IMAGE_NAME}:${VERSION}"
                sh '''
                    docker build -t ${IMAGE_NAME}:${VERSION} .
                '''
            }
        }

        stage('Push to Registry') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag ${IMAGE_NAME}:${VERSION} ${DOCKER_USER}/${IMAGE_NAME}:${VERSION}
                        docker push ${DOCKER_USER}/${IMAGE_NAME}:${VERSION}
                    '''
                }
            }
        }
    }
}
