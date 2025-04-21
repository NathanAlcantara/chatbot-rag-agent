# CI/CD with CircleCI

CircleCI is a cloud-based CI/CD platform that allows teams to automate their software development workflows with ease.

## Key Features
- **Custom Orbs**: Reusable packages of CircleCI configuration.
- **Parallelism**: Run tests and builds faster by executing them in parallel.
- **Docker Support**: Run builds inside Docker containers.

## Example Config

Here's an example CircleCI configuration for a Ruby project:

```yaml
version: 2.1

jobs:
  build:
    docker:
      - image: circleci/ruby:3.0
    steps:
      - checkout
      - run: bundle install
      - run: rake test
```

Save this configuration in `.circleci/config.yml` to enable CI/CD workflows for your project.