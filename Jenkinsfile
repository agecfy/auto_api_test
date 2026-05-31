pipeline {
    agent any
    environment {
        TEST_ENV = 'dev'
    }
    stages {
        stage('Checkout') {
            steps {
                git 'https://your-git-repo-url.git'   // 替换为你的实际仓库地址
            }
        }
        stage('Install Dependencies') {
            steps {
                sh 'python -m pip install -r requirements.txt'
            }
        }
        stage('Run API Tests') {
            steps {
                sh '''
                    pytest testcases/ --alluredir=./reports/allure_raw
                '''
            }
        }
        stage('Generate Allure Report') {
            steps {
                allure includeProperties: false, jdk: '', results: [[path: 'reports/allure_raw']]
            }
        }
    }
    post {
        always {
            cleanWs()
        }
    }
}
