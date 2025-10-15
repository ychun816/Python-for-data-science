# ft_package

A simple example Python package for the Python Piscine project.

## Description
This package contains a single function, `count_in_list()`,  
which counts the number of times a given value appears in a list.

## Example
```python
from ft_package import count_in_list

print(count_in_list(["toto", "tata", "toto"], "toto"))  # Output: 2
print(count_in_list(["toto", "tata", "toto"], "tutu"))  # Output: 0
```

## Structure
```
ex09/
├── ft_package/            # Package folder
│   ├── __init__.py        # Tell Python this is a package
│   └── count_in_list.py   # Function
│
├── pyproject.toml         # Build system config (replaces setup.py)
├── README.md              # Short documentation
├── LICENSE                # Open-source license
└── tester.py              # (optional) for testing package
```

## Test Commands
```
pip show -v ft_package
pip install ./dist/ft_package-0.0.1.tar.gz
pip install ./dist/ft_package-0.0.1-py3-none-any.whl
```