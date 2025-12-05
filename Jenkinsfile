pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'YOUR_DOCKERHUB_USER' 
        IMAGE_NAME = 'devops-lab'
        TAG = 'latest'
    }
    stages {
        stage('Build Image') {
            steps {
                script {
                    sh 'docker build -t $DOCKERHUB_USER/$IMAGE_NAME:$TAG ./app'
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-hub-credentials', passwordVariable: 'DOCKER_PASS', usernameVariable: 'DOCKER_USER')]) {
                    sh 'echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin'
                    sh 'docker push $DOCKERHUB_USER/$IMAGE_NAME:$TAG'
                }
            }
        }
        stage('Deploy to K8s') {
            steps {
                sh 'kubectl apply -f kubernetes/deployment.yaml'
                sh 'kubectl apply -f kubernetes/service.yaml'
            }
        }
    }
}