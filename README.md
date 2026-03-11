# Docker CI/CD Pipeline with AWS EC2 

## Project Overview

This project demonstrates a **complete DevOps CI/CD pipeline** that automatically builds and deploys a containerized Python Flask application to an AWS EC2 instance.

Whenever code is pushed to GitHub, **GitHub Actions automatically builds a Docker image and deploys it to the EC2 server**, ensuring continuous delivery.

---

## Architecture

```
Developer Push Code
        │
        ▼
     GitHub Repository
        │
        ▼
   GitHub Actions CI/CD
        │
        ▼
   Build Docker Image
        │
        ▼
 Deploy to AWS EC2 via SSH
        │
        ▼
 Run Docker Container
        │
        ▼
 Web Application Live
```

---

## Technologies Used

* Python (Flask)
* Docker
* GitHub
* GitHub Actions
* AWS EC2
* CI/CD Pipeline

---

## Project Structure

```
docker-cicd-aws
│
├── .github
│   └── workflows
│       └── deploy.yml
│
├── app.py
├── Dockerfile
└── README.md
```

---

## Application Code

### Python Flask App

```
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Docker CI/CD Deployed Successfully 🚀</h1><p>Docker + GitHub Actions + AWS EC2</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
```

---

## Docker Configuration

### Dockerfile

```
FROM python:3.9-slim

WORKDIR /app

COPY . /app

RUN pip install flask

EXPOSE 80

CMD ["python", "app.py"]
```

---

## CI/CD Pipeline

GitHub Actions automatically runs when code is pushed to the **main branch**.

Pipeline Steps:

1. Checkout repository
2. Connect to EC2 via SSH
3. Stop old container
4. Build Docker image
5. Run new container

---

## Live Application

The application is deployed on AWS EC2 and accessible at:

```
http://13.232.194.97
```

---

## Features

* Automated CI/CD using GitHub Actions
* Docker containerized Python application
* Automatic deployment to AWS EC2
* Continuous Integration and Continuous Delivery workflow

---

## Key Learning Outcomes

Through this project I learned:

* Docker containerization
* GitHub Actions CI/CD automation
* AWS EC2 deployment
* SSH-based remote deployment
* DevOps workflow design

---

## Author

Dheeraj Kumar
Cloud & DevOps Enthusiast
