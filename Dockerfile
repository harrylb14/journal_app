FROM python:3.8.3-alpine

# set work directory
WORKDIR /usr/src/

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN \
 apk add --no-cache postgresql-libs && \
 apk add --no-cache --virtual .build-deps gcc musl-dev postgresql-dev && \
 pip install -r requirements.txt --no-cache-dir && \
 apk --purge del .build-deps

# copy project
COPY . .

ENTRYPOINT ["/usr/src/entrypoint.sh"]