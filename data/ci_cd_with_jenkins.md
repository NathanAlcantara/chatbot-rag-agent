# CI/CD with Jenkins

Jenkins is one of the most popular open-source tools for implementing CI/CD pipelines. It provides extensive flexibility and plugin support.

## Key Features
- **Extensive Plugin Ecosystem**: Over 1,500 plugins available.
- **Declarative Pipelines**: Define pipelines in a readable, YAML-like syntax.
- **Integration**: Supports integration with version control systems, build tools, and deployment tools.

## Example Jenkinsfile

Here's an example of a declarative pipeline for a Java project:

```groovy
pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh 'mvn clean package'
            }
        }

        stage('Test') {
            steps {
                sh 'mvn test'
            }
        }

        stage('Deploy') {
            steps {
                sh './deploy.sh'
            }
        }
    }
}
```

Save the `Jenkinsfile` in your repository's root and configure Jenkins to use it for your pipeline.