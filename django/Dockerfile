# Use an official Python runtime as the parent image
FROM python:3.10.11-slim-buster

# Set environment variables
# Prevents Python from writing pyc files to disc (equivalent to python -B option)
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr (equivalent to python -u option)
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container to /app
WORKDIR /app

# Copy the current directory (host) contents into the container at /app
COPY requirements.txt /app/requirements.txt

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app/

# Run Django's development server when the container launches
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
