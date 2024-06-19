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
6. Navigate to `localhost:8000/docs` to access the swagger UI.
7. Test all the endpoints using the Swagger UI using 'Try it out'.
8. Here are the key endpoints: /place, /left, /right, /move, and /report.
9. The /place endpoint positions the robot at specified coordinates. If invalid coordinates are provided, an error message will be returned in the response.
10. The /left endpoint turns the robot's direction 90 degrees to the left. The response includes the updated coordinates and new direction.
11. The /right endpoint shifts the robot's direction 90 degrees to the right. The response contains the updated coordinates and the new direction.
12. The /move endpoint advances the robot one step in the current direction. The response will show the robot's new coordinates.
13. The /report endpoint displays the robot's current position.

### Using Docker:

1. Make sure Docker is installed on your machine.
2. Clone the git repository.
3. Build the Docker image using `docker build -t <image-name> .`.
4. Run the container using `docker run -p <port-nbr>:80 <image-name>`.
5. Navigate to `0.0.0.0:<port-nbr>/docs` to access the swagger UI.
6. Test all the endpoints using the Swagger UI using 'Try it out'.
7. Here are the key endpoints: /place, /left, /right, /move, and /report.
8. The /place endpoint positions the robot at specified coordinates. If invalid coordinates are provided, an error message will be returned in the response.
9. The /left endpoint turns the robot's direction 90 degrees to the left. The response includes the updated coordinates and new direction.
10. The /right endpoint shifts the robot's direction 90 degrees to the right. The response contains the updated coordinates and the new direction.
11. The /move endpoint advances the robot one step in the current direction. The response will show the robot's new coordinates.
12. The /report endpoint displays the robot's current position.

## Unit test on machine:

1. test_toy_robot.py has the unit tests using pytest.
2. You can run these tests `pytest test_toy_test.py`

## Unit test on docker:

1. Docker image runs tests during the image build process. If any of the tests fail it will not build the image.

### Note: I just added sample Jenkinsfile to demonstate the CI/CD pipeline?

## This is how our Swagger UI running at localhost:8000/docs looks like:

![image](https://github.com/tanvisharma1325/toy_robot_puzzle_solution/assets/173178419/4b1daf38-e3d4-4707-ba36-2a1c4f764e7e)
You can try and test each endpoint "Try it out by expanding each endpoint.

