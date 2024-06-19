pipeline {
    agent any

    stages {
        stage('Pull code from GitHub') {
            steps {
                git 'https://github.com/tanvisharma1325/toy_robot_puzzle_solution.git'
            }
        }

        stage('Install Docker') {
            steps {
                sh 'curl -fsSL https://get.docker.com -o get-docker.sh'
                sh 'sh get-docker.sh'
            }
        }

        stage('Build and Push Docker image') {
            steps {
                script {
                    docker.withRegistry('https://<your-aws-account-id>.dkr.ecr.region.amazonaws.com', 'ecr:region:aws-credentials-id') {
                        def appImage = docker.build("<your-image-name>")
                        appImage.push("your-image-tag")
                    }
                }
            }
        }

        stage('Deploy to ECS') {
            steps {
                sh 'aws ecs update-service --cluster your-cluster-name --service your-service-name --force-new-deployment'
            }
        }
    }
}
