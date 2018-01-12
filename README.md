# Terminal Parking Lot App

A parking lot program in your terminal that can accept file input and user input. This was a project I was expected to complete for a take home project. I liked what I accomplished given the time expected and my noobness in Python so I decided to add this project to my portfolio.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. Please read the PROGRAM_REQUIREMENTS.md file to understand the requirements/expectations of this project.
### Prerequisites

What things you need to install the software and how to install them

```
python3
pip
```

### Installing

Please clone the private repo or download the zip. Feel free to request invitation as a collab.

```
pip install -r requirements.txt
```

## To install requirements and run the tests in one go

```
./Makefile
```

### Unit & Functional tests

The tests cover the create_parking_lot() class and console_app functions. Alternatively, you can also do the following to run tests with coverage:

```
py.test --cov=create_parking_lot --cov=console_app tests/
```

## Running the interactive terminal program

```
./parking_lot
```

## Feeding a file to the terminal program

```
./parking_lot file_inputs.txt
```

## Problems?

Is the program not executable?
```
$ chmod +x myscript.py
```

Is the program being interrupted during runtime and you're on Linux?
Change the path in ./parking_lot

## Authors

* **Tawsif (Sif) Ahmed** - *Initial work* 
If you run into any problems, have any questions, concerns, or comments, feel free to email me directly at ahmedt93@gmail.com

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

