# ShopSphere — DevOps E-Commerce Project

A containerized e-commerce demo application built with Python, Flask, SQLite, and Docker. This project is being developed to demonstrate practical DevOps skills, including automated testing, continuous integration, containerization, deployment, and monitoring.

## Features

- Product catalog
- Shopping cart
- Checkout and order history
- SQLite database with product stock management
- Health-check endpoint
- Automated tests using pytest
- Docker image and persistent database volume

## Technology Stack

- **Application:** Python, Flask
- **Database:** SQLite, Flask-SQLAlchemy
- **Testing:** pytest
- **Containerization:** Docker
- **Version Control:** Git and GitHub
- **Planned DevOps tools:** Jenkins, Docker Hub, Kubernetes, Terraform, AWS, Prometheus, and Grafana

## Project Structure

```text
shopsphere-devops/
├── app/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   └── seed.py
├── scripts/
│   └── init_db.py
├── templates/
├── tests/
│   └── test_app.py
├── Dockerfile
├── entrypoint.sh
├── requirements.txt
└── run.py
```

## Run Locally

### 1. Clone the repository

```bash
git clone https://github.com/JonSOnow/shopsphere-devops.git
cd shopsphere-devops
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, run this for the current terminal session:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
pip install -r requirements.txt
```

### 4. Start the application

```powershell
python run.py
```

Open http://127.0.0.1:5000 in your browser.

## Run Tests

```powershell
python -m pytest -v
```

The current test suite contains six tests covering the homepage, product API, health endpoint, shopping cart, checkout, and order history.

## Run with Docker

Build the image:

```powershell
docker build -t shopsphere:1.0 .
```

Create a persistent database volume:

```powershell
docker volume create shopsphere_data
```

Run the container:

```powershell
docker run -d --name shopsphere-app -p 5000:5000 -v shopsphere_data:/app/instance -e INSTANCE_PATH=/app/instance shopsphere:1.0
```

Check application health:

```powershell
Invoke-RestMethod http://localhost:5000/health
```

View container logs:

```powershell
docker logs shopsphere-app
```

Stop the container:

```powershell
docker stop shopsphere-app
```

## Development Roadmap

- [x] Flask application and basic e-commerce workflows
- [x] Automated test suite
- [x] Docker containerization
- [x] GitHub repository
- [ ] Professional CI pipeline with Jenkins
- [ ] Automated Docker image build and publishing
- [ ] Cloud deployment
- [ ] Kubernetes deployment and configuration
- [ ] Monitoring and logging

## Important Notes

This is a learning and portfolio project, not a production-ready e-commerce service. Authentication, payment integration, CSRF protection, production secret management, and additional security and concurrency controls would be required before real-world production use.

## Repository

https://github.com/JonSOnow/shopsphere-devops
