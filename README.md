# Data Capture

Solution to technical test assigned by the Team International recruiter team.

## Installation
This solution requires a few dependencies that must be installed prior to using it. First install the poetry packaging and dependency manager using the following [instructions](https://python-poetry.org/docs/#installation).

Then, first install python dependencies, include `dev` dependencies
```bash
poetry install
```

The previous command will create a new python environment with the necessary python packages installed.


## Usage
In order to run the tests there are two alternatives
  1. With the command `poetry run pytest`,
  2. or activating the python environment associated with the project through the command `poetry shell` and then just running the command `pytest`.


### Remarks
  * According to official [documentation](https://wiki.python.org/moin/TimeComplexity) accessing any element of a list have constant time complexity.
