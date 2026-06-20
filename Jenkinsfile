pipeline {
	agent any
	environment {
		IMAGE_NAME = "serc-app"
		IMAGE_TAG = "${env.BUILD_NUMBER ?: 'local'}"
	}
	stages {
		stage('Checkout') {
			steps {
				checkout scm
			}
		}
		stage('Install & Test') {
			steps {
				sh 'python3 -m venv .venv || true'
				sh '. .venv/bin/activate && pip install -r src/requirements.txt'
				sh '. .venv/bin/activate && pytest -q'
			}
		}
		stage('Build Docker') {
			steps {
				sh 'docker build -t ${IMAGE_NAME}:${IMAGE_TAG} .'
			}
		}
		stage('Publish (optional)') {
			when {
				expression { return env.DOCKER_REGISTRY != null }
			}
			steps {
				sh 'docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
				sh 'docker push ${DOCKER_REGISTRY}/${IMAGE_NAME}:${IMAGE_TAG}'
			}
		}
	}
	post {
		always {
			cleanWs()
		}
	}
}


