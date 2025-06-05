pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }

        stage('Lint Code') {
            steps {
                sh 'pylint app/ > pylint_report.txt || true'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pytest --junitxml=test_results.xml'
            }
        }

        stage('Archive Results') {
            steps {
                junit 'test_results.xml'
                archiveArtifacts artifacts: 'pylint_report.txt', allowEmptyArchive: true
            }
        }
    }
}
