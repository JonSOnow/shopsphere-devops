
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

        stage('Check Docker') {
            steps {
                bat 'docker version'
            }
        }

        stage('Validate Docker Compose') {
            steps {
                bat 'docker compose config --quiet'
                echo 'Docker Compose configuration is valid'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t shopsphere:ci-%BUILD_NUMBER% .'
            }
        }

        stage('Deploy with Docker Compose') {
            steps {
                bat 'docker compose up -d --build'
            }
        }

        stage('Health Check') {
            steps {
                script {
                    def healthy = false

                    for (int i = 0; i < 12; i++) {
                        def status = bat(
                            script: 'curl.exe -s -o NUL -w "%%{http_code}" http://localhost:8081/health',
                            returnStdout: true
                        ).trim()

                        if (status.endsWith('200')) {
                            healthy = true
                            break
                        }

                        sleep(time: 5, unit: 'SECONDS')
                    }

                    if (!healthy) {
                        bat 'docker compose ps'
                        bat 'docker compose logs --tail 80'
                        error('ShopSphere health check failed')
                    }

                    echo 'ShopSphere health check passed'
                }
            }
        }
    }

    post {
        success {
            echo 'ShopSphere CI, Docker build, Compose deployment, and health check completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
