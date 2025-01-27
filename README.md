# FactHub


 A Dockerized Flask Application for Random Facts
FactHub is a simple Flask web application that delivers random fun and interesting facts. This project demonstrates the use of Flask for web development, Docker for containerization, and GitHub Actions for automating CI/CD workflows.



Features
💡 Random Facts: Provides an endless supply of fun and intriguing facts about science, history, and life.
🚀 Dockerized: The app is fully containerized using Docker for easy portability and scalability.
🤖 Automated CI/CD: Uses GitHub Actions to automate building and pushing Docker images to Docker Hub.



Project Structure:
FactHub/
├── app.py                # Flask application
├── requirements.txt      # Python dependencies
├── templates/
│   └── index.html        # HTML for the web app
├── static/
│   └── styles.css        # CSS for styling
├── Dockerfile            # Docker configuration
└── .github/workflows/
    └── docker-image.yml  # GitHub Actions workflow


How to Run

Option 1: Run Locally

Clone the repository:

git clone https://github.com/sa3id31/facthub
cd facthub

Install dependencies:

pip install -r requirements.txt

Run the Flask app:

python app.py
Open your browser and navigate to http://127.0.0.1:5000.


Option 2: Run Using Docker

Pull the Docker image:

docker pull sa3id31/facthub:latest

Run the Docker container:

docker run -p 5000:5000 sa3id31/facthub
Open your browser and navigate to http://localhost:5000.


This project uses GitHub Actions for CI/CD to:

Build a Docker image from the Dockerfile.
Push the Docker image to Docker Hub.
Workflow file: .github/workflows/docker-image.yml

Technologies Used
Python: Flask web framework.
Docker: Containerization.
GitHub Actions: CI/CD pipeline automation.
