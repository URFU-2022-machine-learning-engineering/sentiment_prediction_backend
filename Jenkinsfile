pipeline {
  agent { label 'h-node' }
  stages {
    stage('prepare') {
    steps {
      sh '''
      docker stop sentiment-prediction-api || exit 0
      docker rmi -f sp-api
      '''
      }
    }
    stage('build') {
      steps {
        sh 'docker build -t sp-api .'
      }
    }

    stage('run') {
      steps {
        sh 'docker run -d --rm --name sentiment-prediction-api -p 8000:8000 sp-api'
      }
    }

    stage('test') {
      steps {
        sh '''
        attempt_counter=0
        max_attempts=10

        until $(curl --output /dev/null --silent --get --fail http://127.0.0.1:8000); do
            if [ ${attempt_counter} -eq ${max_attempts} ];then
              echo "Max attempts reached"
              exit 1
            fi

            printf '.'
            attempt_counter=$(($attempt_counter+1))
            sleep 2
        done

        '''
      }
    }

  }
}
