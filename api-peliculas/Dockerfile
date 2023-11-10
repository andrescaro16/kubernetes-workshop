FROM python:3.11-slim-buster

# Create app directory
RUN mkdir /api-peliculas
# Setup working directory
WORKDIR /api-peliculas
# Install dependencies ubuntu & Curl
RUN apt-get update
RUN apt-get install -y curl
# Copy application
COPY . /api-peliculas/
# Install application dependencies
RUN pip3 install -r /api-peliculas/requirements.txt
# Define environment variable
ENV FLASK_APP "entrypoint.py"
ENV FLASK_ENV "development"
ENV APP_SETTINGS_MODULE "config.default"
ENV PORT 5000
# init bd and create schemas

RUN flask db migrate
RUN flask db upgrade

# expose port
EXPOSE ${PORT}

# init flask with map any ip outside from container
CMD ["flask", "run", "--host","0.0.0.0"]