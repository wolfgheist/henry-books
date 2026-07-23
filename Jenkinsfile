pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'docker compose -f docker-compose-deploy.yml build'
            }
        }

        stage('Deploy') {
            steps {
                sh 'docker compose -f docker-compose-deploy.yml up -d'
            }
        }
    }

    post {
        always {
            sh 'docker compose -f docker-compose-deploy.yml ps'
        }
    }
}