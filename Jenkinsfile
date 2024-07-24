pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8.10'  // Specify the Python version you want to use
        VENV = 'myenv'            // Name of your virtual environment
        DOCKER_REGISTRY = 'docker.io'
        DOCKER_HUB_REPO = 'nithiniast/my-python-app'
        DOCKER_IMAGE_TAG = '1'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository containing main.py, database.py, etc.
                git 'https://github.com/nithinraghu1997/sales_force_api.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                    sh '''pip install -r requirements.txt'''
            }
        }
        stage('Build and Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('https://docker.io', 'Dockerhub') {
                        def dockerImage = docker.build("${DOCKER_HUB_REPO}:${DOCKER_IMAGE_TAG}")
                        dockerImage.push()
                    }
                }
            }
        }
    }

    post {
        always {
            script {
                docker.image("${DOCKER_HUB_REPO}:${DOCKER_IMAGE_TAG}").remove()
            }
        }
    }
}

                
