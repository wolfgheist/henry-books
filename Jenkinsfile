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
                bat 'docker compose -f docker-compose-deploy.yml build'
            }
        }

        stage('Deploy') {
            steps {
                bat 'docker compose -f docker-compose-deploy.yml up -d'
            }
        }
    }

    post {
        always {
            bat 'docker compose -f docker-compose-deploy.yml ps'
        }
    }
}