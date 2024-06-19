# toy_robot_puzzle_solution

This application is built using Python FastAPI.

The file `toy_robot.py` contains the puzzle solution using FastAPI, and `test_toy_robot.py` contains the automated tests to validate the functionality.

## How to Run?

You can run this application in two ways - either on your local machine or using Docker:

### On Your Local Machine:

1. Clone the git repository.
2. Install Python on your machine.
3. Install the FastAPI package using `pip install fastapi`.
4. Install the pytest package using `pip install pytest`.
5. Run the command `uvicorn toy_robot:app`. This will start the uvicorn server on port 8000.
6. Navigate to `localhost:8000/docs`.
7. Test all the endpoints using the Swagger UI.

### Using Docker:

1. Make sure Docker is installed on your machine.
2. Clone the git repository.
3. Build the Docker image using `docker build -t <image-name> .`.
4. Run the container using `docker run -p <port-nbr>:80 <image-name>`.
5. Navigate to `0.0.0.0:<port-nbr>/docs`.
6. Test all the endpoints using the Swagger UI.

## Unit test on machine:

1. test_toy_robot.py has the unit tests using pytest.
2. You can run these tests `pytest test_toy_test.py`

## Unit test on docker:

1. Docker image runs tests during the image build process. If any of the tests fail it will not build the image.

### Note: I just added Jenkinsfile to demonstate. How would create the CI/CD?

## This is how our Jenkinsfile looks like:


