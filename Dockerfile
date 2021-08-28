
# Pull base image
FROM python:3.8



# set default environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV LANG C.UTF-8
ENV DEBIAN_FRONTEND=noninteractive

# set project environment variables
# grab these via Python's os.environ
# these are 100% optional here
ENV PORT=8888

# RUN apt-get update -y
# RUN apt-get install -y  binutils libproj-dev gdal-bin  redis-server  postgresql

# create and set working directory
RUN mkdir /code
WORKDIR /code



# Add current directory code to working directory
ADD . /code/


# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    tzdata \
    python3-setuptools \
    python3-pip \
    python3-dev \
    python3-venv \
    git \
    build-essential \
    python3-wheel \
    python3-cffi \
    libcairo2 \
    libpango-1.0-0  \
    libpangocairo-1.0-0  \
    libgdk-pixbuf2.0-0  \
    libffi-dev  \
    shared-mime-info \
    binutils \ 
    libproj-dev \ 
    gdal-bin \ 
    redis-server\ 
    && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install dependencies
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8888
CMD gunicorn deeptech.wsgi:application --bind 0.0.0.0:$PORT
