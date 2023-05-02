Since python is a dynamically typed language, type errors are possible at runtime.
`mypy` allows you to check python source code for type errors.

# Using mypy

```sh
$ python --version
Python 3.6.0

$ pip install mypy
$ mypy syntax.py
syntax.py:4: error: Unsupported operand types for + ("int" and "str")
syntax.py:8: error: Incompatible return value type (got "str", expected "float")
syntax.py:11: error: Too many arguments for "return_type"
syntax.py:18: error: Too few arguments for "another"
```

# Files in this folder (run `mypy file` to see the output)

- good_example.py: a properly typed fibonnacci function. mypy will produce no output
- syntax.py: shows the syntax for annotating functions
- standard_library.py: importing from the standard library is supported
- mymodule.py, local_imports.py: example of local imports working in mypy
- third_party.py & pandas.pyi: example of using an untyped 3rd-party library and supplying your own types

# Other links

- mypy project: http://mypy-lang.org/
- Emacs integration used in demo: https://github.com/lbolla/emacs-flycheck-mypy/
