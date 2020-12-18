pipeline {
    agent any
    stages {

        stage('Setup Enviroment and Dependencies'){
            steps {
                sh '''
                   chmod +x setup.sh
                   ./setup.sh
                    '''
            }
        }
        stage('Setup Manage and migration'){
            steps {
                sh '''
                   chmod +x migration.sh
                   ./migration.sh
                    '''
            }
        }

         stage('Setup Apache2'){
             steps {
                 sh '''
                    chmod +x apache.sh
                    ./apache.sh
                     '''
             }
         }
    }
}