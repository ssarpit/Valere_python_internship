# Step 1: Use an official lightweight Python image as a parent image
FROM python:3.11-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements file into the container
# This is done first to leverage Docker's layer caching.
# If requirements.txt doesn't change, Docker won't reinstall dependencies on every build.
COPY requirements.txt .

# Step 4: Install the Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy your application code into the container
# This copies the entire 'app' directory and the '.env' file
COPY ./app /app/app
COPY ./.env /app/.env

# Step 6: Expose the port the app runs on
# This tells Docker that the container will listen on port 8000
EXPOSE 8000

# Step 7: Define the command to run your app
# This command starts the Uvicorn server.
# --host 0.0.0.0 is crucial to make the server accessible from outside the container.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
