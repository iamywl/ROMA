// Jenkinsfile
pipeline {
    agent any // Jenkins Agent (단일 EC2 인스턴스이므로 'any'로 시작)

    environment {
        DOCKER_HUB_CREDENTIAL_ID = 'docker-hub-credentials'
        DOCKER_IMAGE_NAME = 'lywdev/roma'
        KUBECONFIG_ID = 'kubernetes-config'
        K8S_MANIFESTS_PATH = 'k8s'
    }

    stages {
        stage('Checkout Code') {
            steps {
                script {
                    echo "Code checked out successfully."
                }
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ."
                    sh "docker build -t ${DOCKER_IMAGE_NAME}:latest ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    withCredentials([usernamePassword(credentialsId: DOCKER_HUB_CREDENTIAL_ID, passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh "docker login -u ${DOCKER_USERNAME} -p ${DOCKER_PASSWORD}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}"
                        sh "docker push ${DOCKER_IMAGE_NAME}:latest"
                    }
                }
            }
        }

        stage('Deploy to Kubernetes (kubectl)') {
            steps {
                script {
                    sh "git config --global user.email 'jenkins@example.com'"
                    sh "git config --global user.name 'Jenkins CI'"

                    dir("${WORKSPACE}") {
                        sh "sed -i 's|image: ${DOCKER_IMAGE_NAME}:latest|image: ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}|g' ${K8S_MANIFESTS_PATH}/deployment.yaml"

                        withCredentials([usernamePassword(credentialsId: 'github-user-pat', passwordVariable: 'GH_PASSWORD', usernameVariable: 'GH_USERNAME')]) {
                            sh "git add ${K8S_MANIFESTS_PATH}/deployment.yaml"
                            sh "git commit -m 'Update ROMA app image tag to ${env.BUILD_NUMBER} by Jenkins'"
                            sh "git push https://${GH_USERNAME}:${GH_PASSWORD}@github.com/iamywl/ROMA.git HEAD:main"
                        }
                    }
                }
            }
        }
    }

    post {
        always {
            echo 'Pipeline finished.'
        }
        failure {
            echo 'Pipeline failed. Check console output for details.'
        }
    }
}
