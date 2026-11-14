# Contributing Guidelines

Thank you for your interest in contributing to this project. We welcome bug reports, documentation improvements, and code contributions.

## Development Workflow

1. **Fork and clone** the repository.
2. **Create a topic branch** from `main`:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. **Install dependencies** using the repository's configured package manager.
4. **Follow conventions**:
   - Adhere to the code style enforced by the repository linter and formatter.
   - Respect instructions documented in `AGENTS.md` and `DESIGN.md` (if applicable).
   - Write unit tests for new logic and bug fixes.
5. **Verify locally** before opening a Pull Request:
   - Run lint, typecheck, and test suites.
   - Ensure the build succeeds without warnings.
6. **Submit a Pull Request**:
   - Provide a clear, concise description of the change.
   - Reference any related issues or discussions.

## Commit Guidelines

Use Conventional Commits format (`feat:`, `fix:`, `docs:`, `refactor:`, `test:`, `chore:`). Keep commit messages focused on intent and outcome.
