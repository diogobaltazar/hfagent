FROM python:3.10

# Set the working directory
WORKDIR /docs

# Copy the documentation source files
COPY docs/python-requirements.txt /docs

# Install requirements from python-requirements.txt
RUN pip install -r python-requirements.txt

# Expose port 8000
EXPOSE 8000

# Default command
CMD ["sphinx-autobuild", "sphinx/source", "sphinx/build", "--host", "0.0.0.0"]
