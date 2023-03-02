# Userinyerface.com Automation Project

This is a test automation project that uses Selenium and Pytest to automate the [UserInyerface](https://userinyerface.com/) website. The Userinyerface website is a gamified user interface where users have to complete various challenges to complete the game. 

## Setup

### Prerequisites

Before running the tests, you need to have the following installed:

* Python 3.6+
* Chrome browser
* ChromeDriver

### Installation

To install the required Python packages, run: `pip install -r requirements.txt`


### Running the tests

To run the tests, execute the following command: `pytest test_process.py`


The tests will run in Chrome browser and will complete the entire game on the Userinyerface.com website.

## Project Structure

* `conftest.py` - contains the Pytest fixtures for browser and Chrome options
* `test_process.py` - contains the main test script that automates the Userinyerface.com game
* `pages` directory - contains the Page Object Model (POM) classes for each step of the game
* `pages/base_page.py` - contains the base POM class that the other POM classes inherit from
* `pages/locators.py` - contains the locators for all the elements on each step of the game
* `avatar.png` - contains the image file that is uploaded in the second step of the game

## Test Process

The automation covers all four stages of the game, including:

1. Password and email entry
2. Image upload and selection of checkboxes
3. Personal information entry and slider movement
4. Selection of all checkboxes and validation of form

## Conclusion

This project provides an example of how to automate tests for a web application using Selenium WebDriver and Python. By using page object design pattern, the code is easy to read, maintain and modify. The Userinyerface website provides a challenging and entertaining interface to test against, making this project a great learning experience for anyone interested in web application testing.

