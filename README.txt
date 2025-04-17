Customer Churn Prediction MLOps Project
Setup

Install dependencies: pip install -r requirements.txt
Initialize DVC: dvc init
Generate data: python data/raw/generate_data.py
Run pipeline: dvc repro

Running Locally

Start services: docker-compose up
Access API at http://localhost:8000
View MLflow UI at http://localhost:5000
View Prometheus at http://localhost:9090
View Grafana at http://localhost:3000 (default login: admin/admin)

Jenkins CI/CD Setup

Configure Jenkins with AWS credentials
Add ECR repository URL in Jenkinsfile
Set up webhook in repository to trigger Jenkins pipeline
Ensure Docker and AWS CLI are installed on Jenkins agent

Deployment

Configure AWS credentials in Jenkins
Update ECR repository URL in Jenkinsfile
Deploy to Elastic Beanstalk or Kubernetes

Monitoring

Grafana dashboard at /var/lib/grafana/dashboards/api_metrics.json
Prometheus scrapes metrics from /metrics endpoint
MLflow tracks model experiments

API Usage
POST to /predict:
{
  "tenure": 12,
  "monthly_charges": 59.99,
  "contract_type": "Month-to-month",
  "internet_service": "Fiber optic",
  "payment_method": "Electronic check"
}

