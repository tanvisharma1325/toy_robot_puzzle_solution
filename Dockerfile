# Use an official Python runtime as a parent image
FROM python:3.11-bullseye

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
ADD . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

RUN pytest -v test_toy_robot.py

# Make port 80 available to the world outside this container
EXPOSE 80

# Run app.py when the container launches
CMD ["uvicorn", "toy_robot:app", "--host", "0.0.0.0", "--port", "80"]