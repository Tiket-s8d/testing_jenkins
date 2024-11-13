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

        stage('Deploy to Kubernetes') {
            steps {
                script {
                    withKubeConfig([credentialsId: 'k3s', serverUrl: 'https://192.168.0.112:6443']) {
                        sh """
                        helm upgrade --install ${HELM_RELEASE} ${HELM_CHART_PATH} \
                            --namespace ${KUBE_NAMESPACE} \
                            --set image.repository=${DOCKER_REGISTRY}/test \
                            --set image.tag=${env.BUILD_ID} \

                        """
                    }
                }
            }
        }
    }


}
