pipeline {
    agent any
    
   environment{
         SONAR_HOME= tool "sonar-scanner"
     }
    stages {
        stage('Code Pull') {
            steps {
                git url: "https://github.com/CDAC-Devops/CDAC-Project.git", branch: "main"
            }
        }
         stage('SonarQube Quality Analysis') {
            steps {
                  withSonarQubeEnv('sonar') {
                   sh '''
                    $SONAR_HOME/bin/sonar-scanner \
                    -Dsonar.projectName=Devops-Pro \
                    -Dsonar.projectKey=Devops-Pro \
                    -Dsonar.host.url=http://192.168.80.253:9000 \
                     -Dsonar.login=squ_95da7900c646424e4a6be8c93cff9b19a090f54b
                '''

                }

            }
        }
         stage('OWASP Dependency check') {
            steps {
                dependencyCheck additionalArguments: '--scan ./', odcInstallation: 'DC'
                dependencyCheckPublisher pattern: '**/dependency-check-report.xml'
            }
        } 
            stage(" Sonarqube Quality Gateway Checks"){
            steps{
                timeout(time: 2, unit: "MINUTES"){                   
                    waitForQualityGate abortPipeline: false
                }
               }
        }
        
        

         stage('Trivy File System Scan') {
            steps {
                 sh 'trivy fs --format table .'
            }
        }
         stage ('docker login') {
            steps {
               script {
                    withCredentials([usernamePassword(credentialsId: 'docker-login', passwordVariable: 'DOCKER_PASSWORD', usernameVariable: 'DOCKER_USERNAME')]) {
                        sh 'echo $DOCKER_PASSWORD | docker login -u $DOCKER_USERNAME --password-stdin'
                    }
              }
            }
             
        }
        
           stage('Building Image And Pushing') {
            steps {
                 sh '/usr/bin/docker image build -t latesh2002/project .'
                 sh '/usr/bin/docker image push latesh2002/project'
            }
        }
        
         
          stage('Run Trivy Image Scan') {
            steps {
                sh 'trivy image --severity CRITICAL,HIGH latesh2002/project:latest'
            }
            
        }
       
           
          stage('Deploying application') {
            steps {
                        sh 'kubectl apply -f ./K8s/deployment.yaml'
                        sh 'kubectl apply -f ./K8s/service.yml'
                        sh 'kubectl apply -f ./K8s/hpa.yml'

            }
            
        }

          stage('checking service and pods') {
            steps {
                sh 'kubectl get pods'
                    sh 'kubectl get svc'
                      sh 'kubectl get hpa'
                
                
            }
            
        } 
        }
    }
