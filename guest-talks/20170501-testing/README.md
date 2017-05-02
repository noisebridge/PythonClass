# Python Testing

Pyclass talk 2017-05-01

# Unittest

Simple JUnit-style tests

- assertTrue
- assertEqual
- assertListEqual

# Pytest

Zero-boilerplate testing

- assert

# Pytest features

- failfast
- suppress io (causes problems with pdb)

# Testing Philosophy

- TDD
- Tests should be simple; don't need conditionals
- Ideally, assertions make it clear what was expected

# Why write tests?

- Tests serve as documentation of expected behavior. Less concrete than implementation.
- They allow code to be refactored. Without them changes could introduce bugs

# Other useful tools

- Static types are an excellent complement to tests
- See notes from last pyclass on python static types

# Coverage

- Useful for understanding what is being tested

# Mock

- Often code uses external services, but we don't necessarily want tests to fail when those services are down!
- Also allows us to be specific about how integration code was called

# Responses

- Specifically solves the http mocking use-case, elegantly

# Hypothesis

- Property-based testing

# Testing in practice

- Run the sentry test suite
- Lint, python, javascript...
- This lessens the burden on maintainers and streamlines contributions

# Integration tests vs unit tests

TODO

# Examples:
- database
- external service
- test as client

