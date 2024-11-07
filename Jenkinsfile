pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Директория для виртуального окружения
        DOCKER_IMAGE = "python:3.9-slim" // Имя Docker-образа
    }

    stages {
        stage('build') {

            steps {
                sh 'docker build -t test .'
            }
        }
    }
}
