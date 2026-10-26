
pipeline {
    agent any

    options {
        timestamps()
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'ShopSphere source code checked out from GitHub'
            }
        }

        stage('Check Python') {
            steps {
                bat '"C:\\Users\\HP\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" --version'
            }
        }

        stage('Create Virtual Environment') {
            steps {
                bat '"C:\\Users\\HP\\AppData\\Local\\Python\\pythoncore-3.15-64\\python.exe" -m venv .venv'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pip install --upgrade pip'
                bat '.venv\\Scripts\\python.exe -m pip install -r requirements.txt pytest'
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest -v'
            }
        }
    }

    post {
        success {
            echo 'ShopSphere CI pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
