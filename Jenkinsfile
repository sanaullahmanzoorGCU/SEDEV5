pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                // Checkout the code from your repository
                checkout scm
            }
        }

        stage('Run Python Script') {
            steps {
                script {
                    // Run the Dec2Hex.py script with a sample input
                    sh 'python3 Dec2Hex.py 255'
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                script {
                    // Run the unit tests
                    sh 'python3 -m unittest test_Dec2Hex.py'
                }
            }
        }
    }

    post {
        always {
            // Clean up or notify based on the build result
            echo 'Pipeline completed.'
        }
    }
}
