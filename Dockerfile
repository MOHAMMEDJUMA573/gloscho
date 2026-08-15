FROM python:3.12-slim-book-worm

RUN python -m venv /venv

ENV PATH=/venv/bin:$PATH

RUN pip install --upgrade pip

#base docker files config
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PYTHONPATH=.

#os dependencies for the docker container
RUN set -eux; \
    apt-get update; \
    apt-get install -y --no-install-recommends \
        # for postgres
        libpq-dev \
        # for Pillow
        libjpeg-dev \
        # for CairoSVG
        libcairo2-dev \
        # build tools
        gcc \
        build-essential; \
    apt-get clean; \
    rm -rf /var/lib/apt/lists/*

RUN mkdir -p /vm
WORKDIR /vm

COPY requirements.txt /tmp/requirements.txt
COPY ./src /vm

ARG DJANGO_DEBUG=0
ARG PROJ_NAME="gloscho"

#execution script
RUN printf "#!/bin/bash\n" > executioner.sh && \
    printf "set -e\n\n" >> executioner.sh && \
    printf "WORKERS=${GUNICORN_WORKERS:-2}" >> executioner.sh && \
    printf "PORT=\"\${PORT:-8080}\"\n\n" >> executioner.sh && \
    printf "python manage.py collectstatic --noinput\n" >> executioner.sh && \
    printf "python manage.py migrate --noinput\n" >> executioner.sh && \
    printf "exec gunicorn gloscho.wsgi --workers 2 --bind 0.0.0.0:8080  \n" >> executioner.sh

RUN chmod +x ./executioner.sh

RUN apt-get remove --purge -y \
    && apt-get autoremove -y \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/

CMD ./executioner.sh