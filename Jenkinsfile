pipeline {
    agent { label "built-in" }
    stages {
        stage("Running tests") {
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
