
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
                bat 'powershell -NoProfile -ExecutionPolicy Bypass -Command "$ok = $false; for ($i = 0; $i -lt 12; $i++) { try { $r = Invoke-WebRequest -Uri http://localhost:8081/health -UseBasicParsing -TimeoutSec 5; if ($r.StatusCode -eq 200 -and $r.Content -match ''healthy'') { $ok = $true; break } } catch {}; Start-Sleep -Seconds 5 }; if (-not $ok) { docker compose ps; docker compose logs --tail 80; exit 1 }; Write-Output ''ShopSphere health check passed''' 
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
