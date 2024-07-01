pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/00casio/quadratic.git'
            }
        }
        stage('Setup') {
            steps {
                sh 'python3 -m venv ${VENV_DIR}'
                sh '. ${VENV_DIR}/bin/activate && pip install --upgrade pip'
                sh '. ${VENV_DIR}/bin/activate && pip install -r requirements.txt'
            }
        }
        stage('Build') {
            steps {
                echo 'Building the Python project...'
                sh '. ${VENV_DIR}/bin/activate && python setup.py build'
            }
        }
        stage('Test') {
            steps {
                echo 'Running tests...'
                sh '. ${VENV_DIR}/bin/activate && pytest tests/'
            }
        }
        stage('Package') {
            steps {
                echo 'Packaging the Python project...'
                sh '. ${VENV_DIR}/bin/activate && python setup.py sdist'
            }
        }
        stage('Deploy') {
            steps {
                echo 'Deploying the Python project...'
                // Add your deployment steps here
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
