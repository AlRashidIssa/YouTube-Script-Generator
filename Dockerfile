# Use an official Arch Linux image as a parent image
FROM archlinux:latest

# Update package database and install necessary packages
RUN pacman -Syu --noconfirm && \
    pacman -S --noconfirm python python-pip gcc && \
    pacman -Scc --noconfirm

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Create and activate a virtual environment
RUN python -m venv venv && \
    /app/venv/bin/pip install --no-cache-dir --upgrade pip && \
    /app/venv/bin/pip install --no-cache-dir -r requirements.txt

# Expose port 5000 to the outside world
EXPOSE 5000

# Run app.py when the container launches
CMD ["/app/venv/bin/python", "app.py"]
