# Python Testing

Pyclass talk 2017-05-01

Covers Python testing tools and philosophy.

Uses a mortgage calculator (calculate_mortgage.py) as the software under test.
Currently all tests pass - edit the source or the tests to make them fail & see output.

(Code requires Python 3.6)

## [Unittest](https://docs.python.org/3/library/unittest.html)

Simple JUnit-style tests.

- assertTrue
- assertEqual
- assertListEqual
- assertRaises

See test_calculate_mortgage_unittest.py.

## [Pytest](https://docs.pytest.org/)

Zero-boilerplate testing.

See test_calculate_mortgage_pytest.py.

- `assert`
- `with pytest.raises(Exception) as exception:`

### Pytest features

- failfast: stop after first failure. Pass `-x` to enable.
- suppress io (cleans up test output but causes problems with pdb; allow `stdin` interaction with `-s`).

## Aside: Why write tests?

- Assurance that your code is working as intended.
- Tests document expected behavior. Less likely to change than implementation.
- They allow code to be refactored. Without them changes could introduce bugs.

## Testing Philosophies

- TDD: test-driven development. Write tests first, then write the minimal amount of code to get tests to pass.
- Tests should be simple; they don't need conditionals (unlike general code).
- Assertions should be specific to make it clear what was expected.

## Integration tests vs unit tests

- Unit tests isolate a specific component.
  - Can be as simple as calling a function with specific arguments and returning a result.
- Integration tests test components of a system working together.
  - Example: tests that check database state, tests that rely on external APIs
    - Sometimes it makes sense to mock these out to allow for more isolated tests
- Both test styles are useful and should be employed.

## [Coverage](https://coverage.readthedocs.io/en/coverage-4.4.1/)

- Useful for understanding what is lacking tests.
- Can be used as an indicator test completeness.

### Usage:

```sh
py.test --cov-report html --cov=calculate_mortgage
open htmlcov/index.html
```

## [Mock](https://docs.python.org/3/library/unittest.mock.html)

- Often code uses external services, but we don't necessarily want tests to fail when those services are down!
- Also allows us to be specific about how integration code was called.

## [Responses](https://github.com/getsentry/responses)

- A python library that mocks requests, elegantly solving the http mocking use-case.
- Works well with a fixtures json directory - capture actual responses helps.

## [Hypothesis](https://github.com/HypothesisWorks/hypothesis-python)

- Property-based testing: the library will generate test inputs given a specification
- Assert that certain assumptions hold:
- In the mortgage calculator case: assert that the monthly mortgage payment is never more than the principal loan amount
  - Turns out this is not the case for high-interest (78%) long-term (100 year) loans
  - (nobody makes loans like that, so I refined the test case to limit morgages to 50 years)

See test_calculate_mortgage_hypothesis.py.

## Technologies related to testing: static analysis

- Linting: enforce a style guide ([see flake8](https://pypi.python.org/pypi/flake8))
  - This lessens the burden on maintainers and streamlines contributions
- Type checking: identify potential errors ([see mypy](https://github.com/python/mypy))
  - Optional types provide correctness benefits and don't inhibit the full dynamic nature of Python
