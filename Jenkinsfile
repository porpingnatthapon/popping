pipeline {
    agent any

    stages {
        stage('Checkout Frontend') {
            steps {
                echo 'Checking out frontend source code...'
            }
        }

        stage('Install & Unit Test') {
            steps {
                echo 'Installing dependencies and running frontend unit tests...'
            }
        }

        stage('Build Frontend') {
            steps {
                echo 'Building frontend...'
            }
        }

        stage('Trigger Integration Tests') {
            steps {
                echo 'Triggering integration pipeline from frontend...'
            }
        }
    }
}
