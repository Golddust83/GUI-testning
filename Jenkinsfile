pipeline {
    agent { label "built-in" }
    stages {
        stage("Run test") {
            steps {
                bat "python -m unittest test_tui"
                echo "Testing" 
            }
        }
    }
    post("Cleanup") {
            always {
                cleanWs() 
                echo "Cleaning up"
            }
        }    
    }
