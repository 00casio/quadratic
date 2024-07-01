pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
        DEPLOY_DIR = "C:\\Users\\User\\Documents\\Stage2024\\deployment\\"' // Change this to your desired deployment directory
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/00casio/quadratic.git'
            }
        }
        stage('Setup') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat '%VENV_DIR%\\Scripts\\activate && pip install --upgrade pip'
                bat '%VENV_DIR%\\Scripts\\activate && pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Python project...'
                bat '%VENV_DIR%\\Scripts\\activate && python setup.py build'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                bat '%VENV_DIR%\\Scripts\\activate && pytest tests\\'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging the Python project...'
                bat '%VENV_DIR%\\Scripts\\activate && python setup.py sdist'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python project locally...'
                bat 'if not exist %DEPLOY_DIR% mkdir %DEPLOY_DIR%'
                bat 'copy dist\\*.tar.gz %DEPLOY_DIR%'
            }
        }
    }
    post {
        always {
            echo 'This will always run'
        }
        success {
            echo 'Pipeline succeeded!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
