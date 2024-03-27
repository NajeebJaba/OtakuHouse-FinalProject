
# Welcome to Otaku House

Otaku House is an e-commerce platform dedicated to fans of anime. Here, you can find a variety of products to show your love for your favorite series and characters.

![Anime Character](image.jpeg)

## Project Overview

This project is an example of QA Automation, focusing on both UI and API Tests, including functional and non-functional tests. Tools like Jenkins for CI/CD and Selenium for parallel testing in different browsers have been integrated.

The website is currently hosted locally. To access it, please download the files from the [GitHub repository](https://github.com/gagishmagi/ecommerce-django-react) and follow the provided instructions.

## Setting Up the Environment

To run the tests, you will need to set up your environment with Selenium and Java. Below are the commands you'll use in your terminal:

### Selenium Setup

- Terminal 1: 
  ```
  pip install selenium
  ```

### Selenium Grid Setup

- Terminal 2:
  ```
  java -jar selenium-server-4.17.0.jar hub
  ```
  
- Terminal 3:
  ```
  java -jar selenium-server-4.17.0.jar node --port 5555 --selenium-manager true
  ```
  
*Note: Java JAR is required and included in the GitHub repository.*

### API Testing Setup

To work with APIs, you need to install the following:

- Terminal:
  ```
  pip install requests
  ```

## Test Structure

The code is structured into three layers:

- **Infra Layer**: Contains the base setup for all tests.
- **Logic Layer**: Where actions for each test are defined.
- **Test Layer**: Different types of tests are executed here.

Each test adheres to the Arrange, Act, Assert (AAA) pattern for consistency and clarity.

## Documentation

The GitHub repository hosts STP (Software Test Plan) and STD (Software Test Description) documents that provide detailed information about the project.

## Contact Information

For any inquiries or suggestions, feel free to open an issue on GitHub or contact me at najeebjabareen@gmail.com.
