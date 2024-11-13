pipeline {
    agent any

    environment {
        DOCKER_REGISTRY = '192.168.0.113:8082'
        KUBE_NAMESPACE = 'test'
        HELM_RELEASE = 'test'
        HELM_CHART_PATH = './test'
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKER_REGISTRY}/test:${env.BUILD_ID}")
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry("http://${DOCKER_REGISTRY}", 'docker-credentials-id') {
                        docker.image("${DOCKER_REGISTRY}/test:${env.BUILD_ID}").push()
                    }
                }
            }
        }
        stage('Setup Kubernetes') {
            steps {
                withCredentials([file(credentialsId: 'KUBECONFIG_CREDENTIALS', variable: 'KUBECONFIG')]) {
                    sh '''
                    echo "Using kubeconfig file: $KUBECONFIG"
                    export KUBECONFIG=$KUBECONFIG
                    kubectl get nodes  # пример использования kubectl
                    '''
                }
            }
        }
        
    }


}
