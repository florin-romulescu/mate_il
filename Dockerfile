# Use the official Python image from the Docker Hub
FROM python:3.10-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && apt-get clean

# Install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . /code/

# Collect static files
RUN python manage.py collectstatic

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Django application
CMD ["gunicorn", "mate_il.wsgi:application", "--bind", "0.0.0.0:8000"]
