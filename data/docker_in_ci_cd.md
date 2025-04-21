# Using Docker in CI/CD Pipelines

Docker simplifies CI/CD pipelines by providing consistent and portable environments for building, testing, and deploying applications.

## Why Use Docker in CI/CD?
- **Consistency**: Eliminate "it works on my machine" issues.
- **Scalability**: Easily run CI/CD jobs in isolated containers.
- **Speed**: Use pre-built Docker images to speed up pipelines.

## Example Workflow

Here's an example of using Docker with GitHub Actions:

```yaml
name: Docker Build and Push

on:
  push:
    branches:
      - main

jobs:
  build:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Build Docker image
        run: docker build -t my-app:latest .

      - name: Push Docker image
        run: docker push my-app:latest
```

Integrate Docker into your CI/CD pipelines to unlock its full potential.