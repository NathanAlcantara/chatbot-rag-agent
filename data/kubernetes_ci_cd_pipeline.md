# Deploying to Kubernetes with a CI/CD Pipeline

Kubernetes simplifies deployment, scaling, and management of containerized applications. Integrating Kubernetes into a CI/CD pipeline automates deployments and increases reliability.

## Key Concepts
- **Manifests**: YAML files defining resources like Pods, Services, and Deployments.
- **kubectl**: Command-line tool to interact with the Kubernetes cluster.

## Example Workflow

Here's an example GitHub Actions workflow for deploying to Kubernetes:

```yaml
name: Deploy to Kubernetes

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v3

      - name: Set up kubectl
        uses: azure/setup-kubectl@v3

      - name: Apply Kubernetes manifests
        run: kubectl apply -f k8s/
```

Use this workflow as a template to deploy your applications to Kubernetes clusters.