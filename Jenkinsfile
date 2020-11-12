pipeline {
    agent any 
    stages {
		stage('checkout') {
            steps {
				echo 'hello world java checked out stage'
				checkout scm
            }
		}
        stage('build and test') {
            steps {
                echo 'hello world java build/test stage'
				sh './gradlew build'
            }
		}
		stage('run') {
            steps {
				echo 'hello world java run stage'
                sh './gradlew run'
            }
        }
    }
}