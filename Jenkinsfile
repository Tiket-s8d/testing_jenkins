pipeline {
    agent any

    environment {
        VENV_DIR = 'venv' // Директория для виртуального окружения
        DOCKER_IMAGE = "python:3.9-slim" // Имя Docker-образа
    }

    stages {
        stage('Setup in Docker') {
            agent {
                docker {
                    image 'python:3.9-slim' // Использование Docker-образа
                    label 'docker' // Можно указать метку, если нужно
                    args '-v /tmp:/tmp' // Опционально: монтируем тома, если нужно
                }
            }
            steps {
                echo 'Setting up Python environment inside Docker...'
                // Устанавливаем зависимости и настраиваем окружение внутри Docker
                sh '''
                    python -m venv ${VENV_DIR}
                    source ${VENV_DIR}/bin/activate  # Для Linux/Mac
                    pip install -r requirements.txt
                '''
            }
        }
    }
}
