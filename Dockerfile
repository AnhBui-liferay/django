# Use official Python image
FROM python:3.11

# Set work directory
WORKDIR /app

# Copy project files
COPY . /app/

# Install dependencies
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Expose port
EXPOSE 8000

# Run Django server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
