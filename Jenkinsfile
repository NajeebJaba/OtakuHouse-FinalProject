pipeline {
    agent any
    environment {
        // Define the Python virtual environment directory
        VENV_DIR = 'venv'
        // Define the path to the Python executable
        PYTHON_PATH = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        // Define the directory where the HTML report is generated
        HTML_REPORT_DIR = "reports"
        // Define the path to the test_runner.py within the test layer directory
        TEST_RUNNER_PATH = "test\\test_runner.py"
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
                    // Navigate to the project root directory in the workspace
                    bat "cd ${WORKSPACE}"
                    // Create the virtual environment if it doesn't exist
                    bat "if not exist ${VENV_DIR} ${PYTHON_PATH} -m venv ${VENV_DIR}"
                    // Activate the virtual environment
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    // Upgrade pip
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    // Install dependencies from requirements.txt
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r ${WORKSPACE}\\requirements.txt"
                }
            }
        }
        stage('Run Tests') {
            steps {
                script {
                    // Activate the virtual environment and set the Python path
                    bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    set PYTHONPATH=%PYTHONPATH%;${WORKSPACE}
                    // Run the tests using the test runner script
                    ${VENV_DIR}\\Scripts\\python ${WORKSPACE}\\${TEST_RUNNER_PATH}
                    """
                }
            }
        }
        stage('List Report') {
            steps {
                script {
                    // List the content of the HTML report directory
                    bat "dir ${WORKSPACE}\\${HTML_REPORT_DIR}"
                }
            }
        }
        stage('Publish Report') {
            steps {
                // Publish the HTML report
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${WORKSPACE}\\${HTML_REPORT_DIR}",
                    reportFiles: 'arcane_report.html',
                    reportName: "HTML Report"
                ]
            }
        }
        stage('Verify Report') {
            steps {
                script {
                    // Display the HTML report content
                    bat "type ${WORKSPACE}\\${HTML_REPORT_DIR}\\arcane_report.html"
                }
            }
        }
        stage('Archive Reports') {
            steps {
                // Archive the HTML report files
                archiveArtifacts artifacts: "${HTML_REPORT_DIR}\\*", allowEmptyArchive: true
            }
        }
    }
}
