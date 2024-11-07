pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Директория для виртуального окружения
        DOCKER_IMAGE = "my-web-app:${env.BUILD_ID}" // Имя Docker-образа с версией сборки
    }

    stages {
        docker {
            image 'python:3.9-slim' // Python-образ для запуска контейнера
        }

        stage('Setup') {
            steps {
                
                echo 'Setting up Python environment...'
                // Создание виртуального окружения и установка зависимостей
                sh 'python -m venv ${VENV_DIR}'
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'

                
            }
        }        
    }
}
