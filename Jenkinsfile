// Jenkinsfile (최종 통합 버전 - sed 명령 수정)
pipeline {
    agent any // Jenkins Agent (단일 EC2 인스턴스이므로 'any'로 시작)

    environment {
        DOCKER_HUB_CREDENTIAL_ID = 'docker-hub-credentials'
        DOCKER_IMAGE_NAME = 'lywdev/roma' // 여러분의 Docker Hub 사용자 이름/저장소 이름을 입력하세요.
        KUBECONFIG_ID = 'kubernetes-config' // 현재 사용되지 않지만, 나중에 kubectl apply 등을 위한 변수
        K8S_MANIFESTS_PATH = 'k8s' // Kubernetes YAML 파일들이 있는 경로
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
                    // Dockerfile이 ROMA 프로젝트 루트에 있다면
                    sh "docker build --no-cache -t ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER} ${WORKSPACE}"
                    sh "docker build --no-cache -t ${DOCKER_IMAGE_NAME}:latest ${WORKSPACE}"
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                script {
                    // Docker Hub에 로그인하여 이미지 푸시
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
                    // Git 커밋을 위한 사용자 정보 설정
                    sh "git config --global user.email 'jenkins@example.com'"
                    sh "git config --global user.name 'Jenkins CI'"

                    // 이미 Jenkins 워크스페이스에 체크아웃된 코드 사용
                    dir("${WORKSPACE}") { // 현재 작업 디렉토리 (워크스페이스)
                        // deployment.yaml 파일 수정 (Docker 이미지 태그를 현재 빌드 번호로 업데이트)
                        // 'image: lywdev/roma:' 뒤에 오는 모든 태그를 현재 빌드 번호로 교체
                        sh "sed -i 's|image: ${DOCKER_IMAGE_NAME}:.*|image: ${DOCKER_IMAGE_NAME}:${env.BUILD_NUMBER}|g' ${K8S_MANIFESTS_PATH}/deployment.yaml"

                        // 변경사항을 Git에 커밋하고 푸시
                        // github-user-pat Credential (GitHub 사용자 이름 + PAT) 사용
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
