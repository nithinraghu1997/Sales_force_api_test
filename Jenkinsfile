pipeline {
    agent any

    environment {
        // Define Docker Hub credentials ID and Docker Hub repository
        DOCKERHUB_CREDENTIALS = 'Docker access'
        DOCKERHUB_REPO = 'nithiniast/my-python-app'
        DOCKER_IMAGE_TAG = '1'
    }

    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image
                    sudo docker.build("${DOCKERHUB_REPO}:${DOCKER_IMAGE_TAG}")
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                script {
                    // Push the Docker image to Docker Hub
                    docker.withRegistry('https://registry-1.docker.io/v1/', DOCKERHUB_CREDENTIALS) {
                        def dockerImage = docker.image("${DOCKERHUB_REPO}:${DOCKER_IMAGE_TAG}")
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        success {
            echo "Docker image pushed successfully to ${DOCKERHUB_REPO}:${DOCKER_IMAGE_TAG}"
        }
    }
}
