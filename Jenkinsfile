pipeline {
    agent any
    environment {
        DOCKERHUB_USER = 'abdullahjabbar73' 
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
    script {
        echo "Deploying to Kubernetes..."
        // Simulating deploy because Jenkins runs inside Docker
        sh 'echo "kubectl apply -f kubernetes/deployment.yaml"'
        sh 'echo "kubectl apply -f kubernetes/service.yaml"'
    }
}
        }
    }

}

