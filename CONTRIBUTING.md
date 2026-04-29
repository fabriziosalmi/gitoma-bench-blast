# Contributing to gitoma-bench-blast

Welcome! We welcome contributions from everyone interested in improving `gitoma-bench-blast`. If you'd like to contribute, please read this guide.

## How to Contribute

Contributions are valuable and greatly appreciated. Here’s how you can help:

### 🐛 Bug Reports
If you find a bug, please follow these steps:
1.  **Reproduce the issue:** Provide clear, minimal steps to reproduce the bug.
2.  **Report details:** Include environment information (OS, Python version, dependencies) and any relevant logs or stack traces.
3.  **Describe the expected vs. actual behavior.**

### ✨ Feature Requests
If you have an idea for a new feature:
1.  Describe the feature clearly.
2.  Explain why it would be beneficial to the project.
3.  If possible, suggest how it could be implemented.

### 💻 Code Contributions
If you are ready to submit code changes:
1.  Fork the repository.
2.  Clone your fork locally.
3.  Create a new branch for your changes (e.g., `git checkout -b feature/my-new-thing`).
4.  Implement your changes, ensuring you keep existing tests passing.
5.  Write tests for any new features or fixes you introduce.
6.  Push your branch and open a Pull Request against the main branch.

## Development Workflow

We use a standard workflow:
1.  **Develop locally:** Work on your feature/fix branch.
2.  **Test thoroughly:** Run the existing test suite (`pytest`) to ensure no regressions are introduced.
3.  **Commit cleanly:** Ensure your commits are atomic and follow the [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/) specification (e.g., `feat: added user profile endpoint`, `fix: corrected off-by-one error`).
4.  **Submit PR:** Open a Pull Request when ready for review.

## Coding Standards
*   Follow PEP 8 style guidelines for Python code.
*   Keep changes minimal and focused on the task at hand.
*   Ensure all new code paths are covered by tests.