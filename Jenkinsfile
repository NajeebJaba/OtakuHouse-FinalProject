pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the project's root directory
        PROJECT_ROOT = "C:\\Users\\ASUS\\OneDrive\\מסמכים\\GitHub\\OtakuHouse-FinalProject"
        // Define the path to the Python executable
        PYTHON_PATH = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        // Define the directory where the HTML report is generated
        HTML_REPORT_DIR = "reports"
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
                    bat "cd ${PROJECT_ROOT}"
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
                    set PYTHONPATH=%PYTHONPATH%;${PROJECT_ROOT}
                    ${VENV_DIR}\\Scripts\\python -m pytest ${PROJECT_ROOT}\\tests\\tests_api\\updateProfile_testAPI.py --html=${PROJECT_ROOT}\\${HTML_REPORT_DIR}\\arcane_report.html
                    """
                }
            }
        }
        stage('List Report') {
            steps {
                script {
                    bat "dir ${PROJECT_ROOT}\\${HTML_REPORT_DIR}"
                }
            }
        }
        stage('Publish Report') {
            steps {
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${PROJECT_ROOT}\\${HTML_REPORT_DIR}",
                    reportFiles: 'arcane_report.html',
                    reportName: "HTML Report"
                ]
            }
        }
        stage('Verify Report') {
            steps {
                script {
                    bat "type ${PROJECT_ROOT}\\${HTML_REPORT_DIR}\\arcane_report.html"
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
