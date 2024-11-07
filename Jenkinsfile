pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Директория для виртуального окружения
        DOCKER_IMAGE = "my-web-app:${env.BUILD_ID}" // Имя Docker-образа с версией
    }

    stages {
        stage('Setup') {
            steps {
                echo 'Setting up Python environment...'
                // Установка Python и создание виртуального окружения
                sh 'python3 -m venv ${VENV_DIR}'
                // Установка зависимостей
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Lint') {
            steps {
                echo 'Running linter...'
                // Запуск линтера (flake8)
                sh '. ${VENV_DIR}/bin/activate && flake8 .'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                // Сборка Docker-образа для приложения
                sh "docker build -t ${DOCKER_IMAGE} ."
            }
        }
  
    }

    post {
        always {
            echo 'Cleaning up...'
            // Очистка рабочей директории
            deleteDir()
        }
    }
}
