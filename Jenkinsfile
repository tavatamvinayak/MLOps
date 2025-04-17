pipeline {
    agent any
    environment {
        AWS_REGION = 'us-east-1'
        ECR_REGISTRY = '<your-ecr-repo>'
        DOCKER_IMAGE = "${ECR_REGISTRY}:latest"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Run Tests') {
            steps {
                sh 'python -m pytest'
            }
        }
        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${DOCKER_IMAGE} .'
            }
        }
        stage('Push to ECR') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', 
                                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh '''
                        aws ecr get-login-password --region ${AWS_REGION} | \
                        docker login --username AWS --password-stdin ${ECR_REGISTRY}
                        docker push ${DOCKER_IMAGE}
                    '''
                }
            }
        }
        stage('Deploy to Elastic Beanstalk') {
            steps {
                withCredentials([[$class: 'AmazonWebServicesCredentialsBinding', 
                                accessKeyVariable: 'AWS_ACCESS_KEY_ID', 
                                secretKeyVariable: 'AWS_SECRET_ACCESS_KEY']]) {
                    sh '''
                        eb init -p docker churn-prediction --region ${AWS_REGION}
                        eb deploy
                    '''
                }
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}