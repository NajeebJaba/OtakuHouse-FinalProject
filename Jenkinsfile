// pipeline {
//     agent any
//
//     environment {
//         //API_KEY= '46e29623-4a45-46d5-83ca-8acc2be72534'
//     }
//
//     stages {
//         stage('Checkout') {
//             steps {
//                 checkout scm
//             }
//         }
//         stage('Prepare') {
//             steps {
//                 echo 'setting up Python environment.......'
//                 sh 'python3 -m venv venv'
//                 sh '. venv/bin/activate'
//                 sh 'pip install requests'
//
//
//         stage('Test') {
//             steps {
//                 echo 'run tests for OtakuHouse ..'
//                 sh """
//                 . venv/bin/activate
//             }
//         }
//         stage('Deploy') {
//             steps {
//                 echo 'Deploying..'
//             }
//         }
//     }
// }




pipeline {
    agent any
    environment {
        // Python virtual environment directory for isolated dependencies
        VENV_DIR = 'venv_magic'
        // The lair of your project's heart
        PROJECT_ROOT = "C:\Users\ASUS\OneDrive\מסמכים\GitHub\OtakuHouse-FinalProject" //"C:\\Users\\ASUS\\OneDrive\\Documents\\GitHub\\OtakuHouse-FinalProject"
        // The path to the almighty Python
        PYTHON_PATH = "C:\\Users\\ASUS\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
        // Where the tales of tests are told
        TALES_DIR = "tales_of_testing"
    }
    stages {
        stage('Gathering Scrolls') {
            steps {
                echo 'Engaging SCM to gather the latest scrolls...'
                checkout scm
            }
        }
        stage('Concocting Potions') {
            steps {
                script {
                    bat "cd ${PROJECT_ROOT}"
                    bat "if not exist ${VENV_DIR} call \"%PYTHON_PATH%\" -m venv ${VENV_DIR}"
                    bat "call ${VENV_DIR}\\Scripts\\activate"
                    bat "call ${VENV_DIR}\\Scripts\\python.exe -m pip install --upgrade pip"
                    bat "call ${VENV_DIR}\\Scripts\\pip install -r potions.txt"
                }
            }
        }
        stage('Chanting Spells') {
            steps {
                script {
                    bat """
                    call ${VENV_DIR}\\Scripts\\activate
                    set PYTHONPATH=%PYTHONPATH%;${PROJECT_ROOT}
                    ${VENV_DIR}\\Scripts\\python -m pytest ${PROJECT_ROOT}\\tests\\wizardry_tests\\profile_enchantment_test.py --html=${PROJECT_ROOT}\\${TALES_DIR}\\arcane_report.html
                    """
                }
            }
        }
        stage('Cataloging Tomes') {
            steps {
                script {
                    bat "dir ${PROJECT_ROOT}\\${TALES_DIR}"
                }
            }
        }
        stage('Showcasing Arcane Knowledge') {
            steps {
                publishHTML target: [
                    allowMissing: false,
                    alwaysLinkToLastBuild: true,
                    keepAll: true,
                    reportDir: "${PROJECT_ROOT}\\${TALES_DIR}",
                    reportFiles: 'arcane_report.html',
                    reportName: "Arcane Testing Chronicles"
                ]
            }
        }
        stage('Deciphering Ancient Texts') {
            steps {
                script {
                    bat "type ${PROJECT_ROOT}\\${TALES_DIR}\\arcane_report.html"
                }
            }
        }
        stage('Ensuring Legacy') {
            steps {
                archiveArtifacts artifacts: "${TALES_DIR}\\*", allowEmptyArchive: false
            }
        }
    }
}
