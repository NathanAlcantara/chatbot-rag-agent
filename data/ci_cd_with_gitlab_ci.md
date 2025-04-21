# CI/CD with GitLab CI

GitLab CI/CD is a built-in feature of GitLab that allows you to define and manage CI/CD pipelines using YAML configuration files.

## Key Features
- **GitLab Runners**: Execute jobs defined in the pipeline.
- **YAML Configuration**: Define pipelines in `.gitlab-ci.yml`.
- **Built-in Docker Support**: Use Docker containers for your builds.

## Example `.gitlab-ci.yml`

Here's an example CI/CD pipeline for a Python project:

```yaml
stages:
  - test
  - build

test:
  stage: test
  image: python:3.10
  script:
    - pip install -r requirements.txt
    - pytest

build:
  stage: build
  script:
    - echo "Building the application..."
```

Save the `.gitlab-ci.yml` file in the root of your repository to enable GitLab CI/CD. GitLab will automatically detect and execute the pipeline.