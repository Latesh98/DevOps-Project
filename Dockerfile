# Use the official Python image from Docker Hub
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .
# Install dependencies
RUN pip install Django
RUN python -m pip install Pillow
# Expose the port the app runs on
EXPOSE 8000
# Run migrations to set up the database and start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
