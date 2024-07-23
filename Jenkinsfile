pipeline {
    agent any
    
    environment {
        PYTHON_VERSION = '3.8.10'  // Specify the Python version you want to use
        VENV = 'myenv'            // Name of your virtual environment
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
                    sh '''sudo apt install -r requirements.txt'''
            }
        }
        stage('Execute Scripts') {
            steps {
                // Run your Python scripts
                    sh "python3 app.py"
                
            }
        }
    }
    
    }
