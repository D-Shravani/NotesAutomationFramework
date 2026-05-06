pipeline {

    agent any

    stages {

        stage('Go To Project Folder') {

            steps {

                dir('C:\\Users\\dsaik\\OneDrive\\Desktop\\NotesAutomationFramework') {

                    bat 'dir'
                }
            }
        }

        stage('Install Dependencies') {

            steps {

                dir('C:\\Users\\dsaik\\OneDrive\\Desktop\\NotesAutomationFramework') {

                    bat 'venv\\Scripts\\python.exe -m pip install -r requirements.txt'
                }
            }
        }

        stage('Run Tests in Parallel') {

            steps {

                dir('C:\\Users\\dsaik\\OneDrive\\Desktop\\NotesAutomationFramework') {

                    bat 'venv\\Scripts\\python.exe -m pytest tests -n 2 --html=reports/report.html --alluredir=allure-results'
                }
            }
        }

        stage('Archive Reports') {

            steps {

                dir('C:\\Users\\dsaik\\OneDrive\\Desktop\\NotesAutomationFramework') {

                    archiveArtifacts artifacts: 'reports/*, screenshots/*, allure-results/*', allowEmptyArchive: true
                }
            }
        }
    }
}