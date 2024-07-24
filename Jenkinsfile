pipeline {
    agent any
    
    environment {
        VENV = 'myenv'                      // Name of your virtual environment
        DOCKER_REGISTRY = 'nithiniast'  // Docker registry username or hostname
        IMAGE_NAME = 'myapp'                // Docker image name
        BUILD_NUMBER = '1'
    }
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout your repository containing main.py, database.py, etc.
                git 'https://github.com/nithinraghu1997/sales_force_api.git'
            }
        }
        
        stage('Setup Environment') {
            steps {
                // Install Python and create virtual environment
                sh '''
                    python3 -m venv ${VENV}
                    source ${VENV}/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                // Build Docker image
                sh "docker build -t ${DOCKER_REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER} ."
            }
        }
        
        stage('Push to Docker Registry') {
            steps {
                // Push Docker image to registry
                sh "docker login -u ${nithiniast} -p ${IAST@1234}"
                sh "docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${BUILD_NUMBER}"
            }
        }
