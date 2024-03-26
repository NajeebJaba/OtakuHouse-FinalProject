pipeline {
    agent any
    environment {
        VENV_DIR = 'venv'
        PYTHON_PATH = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        HTML_REPORT_DIR = "reports"
        // Assuming the test_runner.py is in the 'test' directory
        TEST_RUNNER = "test\\test_runner.py"
    }
    stages {
        stage('Preparation') {
            steps {
                echo 'Checking out SCM'
                checkout scm
            }
        }
        stage('Setup Python Environment') {
            steps {
                script {
                    bat "cd ${WORKSPACE}"
                    bat "if not exist ${VENV_DIR} ${PYTHON_PATH} -m venv ${VENV_DIR}"
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    set PYTHONPATH=%PYTHONPATH%;${WORKSPACE}
                    ${VENV_DIR}\\Scripts\\python ${TEST_RUNNER} --html=${WORKSPACE}\\${HTML_REPORT_DIR}\\report.html
                    """
                }
            }
        }
        stage('List Report') {
            steps {
                script {
                    bat "dir ${WORKSPACE}\\${HTML_REPORT_DIR}"
                }
            }
        }
        stage('Publish Report') {
            steps {
                // The 'publishHTML' step here assumes the HTML Publisher plugin is installed
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${WORKSPACE}\\${HTML_REPORT_DIR}",
                    reportFiles: 'report.html',
                    reportName: "HTML Report"
                ]
            }
        }
        stage('Verify Report') {
            steps {
                script {
                    bat "type ${WORKSPACE}\\${HTML_REPORT_DIR}\\report.html"
                }
            }
        }
        stage('Archive Reports') {
            steps {
                archiveArtifacts artifacts: "${HTML_REPORT_DIR}\\*", allowEmptyArchive: true
            }
        }
    }
}
