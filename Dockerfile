# Use official Ubuntu base image
FROM ubuntu:20.04

# Install Python and pip
RUN apt-get update && apt-get install -y python3-pip

# Set the working directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt /app/
RUN pip3 install -r requirements.txt

# Copy the rest of your application
COPY . /app


EXPOSE 8000
EXPOSE 8501
EXPOSE 8080


# Copy the entrypoint script
COPY entrypoint.sh /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh
# Expose the ports for FastAPI and Streamlit
EXPOSE 8000
EXPOSE 8501

# Set the entrypoint to the entrypoint.sh script
ENTRYPOINT ["/app/entrypoint.sh"]