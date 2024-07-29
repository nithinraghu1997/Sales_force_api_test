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
                    sudo dockerImage = docker.build registry
                }                
            }
        }
        stage ('Push to DockerHub') {
            steps {
                script {
                    sudo docker.withRegistry('', registryCredential){
                    sudo dockerImage.push()
                    }
                }
            }
        }
        stage ('Docker deploy to Container') {
            steps {
                script {
                    sudo docker.withRegistry('', registryCredential){
                    sh "sudo docker run -d --name pythontest -p 8070:5000 nithiniast/pythonapptest" 
                    }
                }
            }
        }
    }
    
    }
