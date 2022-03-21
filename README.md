# Project Description

The goal of this project is to a generic program that parses JSON Data.

## Installation Using a Python Virtual Environment

To get this project running, you require Python 3.8+ You can download it [here](https://www.python.org/downloads/release).

### To Setup a Python 3  Virtual  Environment
After you have installed Python, you can run the following in your Terminal (make sure you are in the root folder)

```python3 -m venv /path/to/new/virtual/environment```

Example:

```python3 -m venv venv```

This creates a new Python virtual environment for us.

### Activate Virtual Environment

Run the following in your Command prompt /Terminal

#### For Windows [Powershell]
```bash
source /path/to/new/virtual/environment/Scripts/activate
```
Example:
```bash
venv/Scripts/activate
```

#### For Linux and MacOS
```bash
source /path/to/new/virtual/environment/bin/activate
```
Example:

```bash
source venv/bin/activate
```

### Install necessary Libraries
After activating the virtual environment, you need to install necessary libraries for the app to work. To achieve this, run:

```bash
python -m pip install -r requirements.txt
```
## Example

After you have successfully set up the environment, you can run the program from the terminal/command-line


```python3 main.py```

The output of the 2 data files can be seen in the schema folder
