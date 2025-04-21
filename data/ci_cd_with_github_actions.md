# CI/CD with GitHub Actions

GitHub Actions is a powerful CI/CD tool integrated directly into GitHub repositories. It allows you to automate workflows such as testing, building, and deploying code.

## Key Features
- **YAML-based workflows**: Define workflows in `.github/workflows` directory.
- **Integration with GitHub**: Respond to events like pull requests, commits, or issue creation.
- **Reusable Actions**: Use community-developed actions to accelerate your development.

## Example Workflow

Here's an example of a GitHub Actions workflow for a Node.js project:

```yaml
name: Node.js CI

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

      - name: Setup Node.js
        uses: actions/setup-node@v3
        with:
          node-version: "16"

      - name: Install dependencies
        run: npm install

      - name: Run tests
        run: npm test
```

Start by creating your workflows in the `.github/workflows` directory to unlock the power of GitHub Actions.