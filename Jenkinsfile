pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8.10'  // Specify the Python version you want to use
        VENV = 'myenv'            // Name of your virtual environment
        registry = 'nithiniast/pythonapptest'
        registryCredential = 'dockerhub_id'
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
        stage('Build Docker Image') {
            steps {
                script {
                    dockerImage = docker.build registry
                }                
            }
        }
        stage ('Push to DockerHub') {
            steps {
                script {
                    docker.withRegistry('', registryCredential){
                    dockerImage.push()
                    }
                }
            }
        }
        stage ('Docker deploy to Container') {
            steps {
                script {
                    docker.withRegistry('', registryCredential){
                    sh "docker run -d --name pythontest3 -p 8070:5000 nithiniast/pythonapptest" 
                    }
                }
            }
        }
    }
}
