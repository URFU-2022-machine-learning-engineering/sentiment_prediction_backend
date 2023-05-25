pipeline {
  agent any
  stages {
    stage('build') {
      steps {
        sh 'docker build -t api .'
      }
    }

    stage('run') {
      steps {
        sh 'docker run -d --name ml_urfu -p 80:8000 api'
      }
    }

    stage('test') {
      steps {
        sh 'curl 127.0.0.1:80'
      }
    }

  }
}