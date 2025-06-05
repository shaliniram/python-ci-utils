pipeline {
    agent any

    stages {
        stage('Install Dependencies') {
            steps {
                bat 'pip install -r requirements.txt'
            }
        }

        stage('Lint Code') {
            steps {
                bat 'pylint app > pylint_report.txt || exit 0'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'pytest --junitxml=test_results.xml'
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
