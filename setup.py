from setuptools import setup, find_packages

setup(
    name="pymonkay",  # Package name (how users will install it: pip install pymonkay)
    version="0.1.0",    # Version number
    packages=find_packages(),
    install_requires=[
    ],
    entry_points={
        "console_scripts": [
            "pymonkay = pymonkay.main:main",   # Entry point to run your CLI tool
        ]
    },
    # ... other metadata (description, author, etc.)
)